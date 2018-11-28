#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <algorithm>

#include <memory.h>

#define INPUT_FILE "B-small-attempt0.in"

using namespace std;

int main()
{
	FILE* fin=fopen(INPUT_FILE,"r");
	char output_file[1024];
	char log_file[1024];
	strcpy(output_file,INPUT_FILE);
	strcpy(strrchr(output_file,'.'),".out");
	strcpy(log_file,INPUT_FILE);
	strcpy(strrchr(log_file,'.'),".log");
	FILE* fout=fopen(output_file,"w");
	FILE* flog=fopen(log_file,"w");

	int num_cases;
	fscanf(fin,"%d",&num_cases);
	for(int k=0;k<num_cases;++k)
	{
		int num_boosters,build_time,num_stars,num_courses;
		int courses[1000],course_sum=0;

		fscanf(fin,"%d %d %d %d",&num_boosters,&build_time,&num_stars,&num_courses);
		for(int i=0;i<num_courses;++i)
		{
			fscanf(fin,"%d",&courses[i]);
			course_sum+=courses[i];
		}

		int noacc_dist=build_time/2;
		int noacc_laps=noacc_dist/course_sum,noacc_rem=noacc_dist%course_sum,noacc_end,accable_portion;
		for(int sum=0,i=0;i<num_courses;++i)
		{
			if(noacc_rem<=sum+courses[i])
			{
				noacc_end=i;
				accable_portion=courses[i]-(noacc_rem-sum);
				break;
			}
			sum+=courses[i];
		}

		int full_course=num_stars/num_courses,rem_course=num_stars%num_courses;
		int course_reps[1000],accable_reps[1000],noacc_time=0;
		for(int i=0;i<num_courses;++i)
		{
			accable_reps[i]=course_reps[i]=full_course+((i<rem_course)?1:0);
			accable_reps[i]-=noacc_laps+((i<=noacc_end)?1:0);
			noacc_time+=(course_reps[i]*courses[i])*2;
		}

		if(num_boosters==0)
		{
			printf("Case #%d: %d\n",k+1,noacc_time);
			fprintf(fout,"Case #%d: %d\n",k+1,noacc_time);
			continue;
		}

		int course_sort[1001];
		for(int i=0;i<num_courses;++i) course_sort[i]=i;
		for(int i=0;i<num_courses;++i)
		{
			int max=i;
			for(int j=i+1;j<num_courses;++j)
			{
				if(courses[course_sort[j]]>courses[course_sort[max]])
				{
					max=j;
				}
			}
			swap(course_sort[i],course_sort[max]);
		}

		int ptr=0,csel=course_sort[ptr],acc_time=noacc_time;
		int easy_boosters=num_boosters-1;
		while(easy_boosters>0)
		{
			while(ptr<num_courses && accable_reps[csel]==0)
			{
				csel=course_sort[++ptr];
			}
			if(ptr>=num_courses) break;

			if(accable_reps[csel]<=easy_boosters)
			{
				acc_time-=accable_reps[csel]*courses[csel];
				easy_boosters-=accable_reps[csel];
				accable_reps[csel]=0;
			} else {
				acc_time-=easy_boosters*courses[csel];
				accable_reps[csel]-=easy_boosters;
				easy_boosters=0;
			}
		}
		while(ptr<num_courses && accable_reps[csel]==0)
		{
			csel=course_sort[++ptr];
		}

		if(ptr<num_courses && accable_reps[csel]>0 && courses[csel]>accable_portion)
		{
			acc_time-=courses[csel];
		} else {
			acc_time-=accable_portion;
		}
		printf("Case #%d: %d\n",k+1,acc_time);
		fprintf(fout,"Case #%d: %d\n",k+1,acc_time);
	}
	fclose(flog);
	fclose(fout);
	fclose(fin);
}
