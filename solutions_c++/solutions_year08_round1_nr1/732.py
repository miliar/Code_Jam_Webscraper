#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;

int main(int argc,char** argv){
	FILE* fin=fopen("input.txt","r");
	FILE* fout=fopen("output.txt","w");
	int cases;
	int len;
	int tmp;
	long int result;
	fscanf(fin,"%d",&cases);
	for(int i=0;i<cases;i++){
		fscanf(fin,"%d",&len);
		vector<int> v1(len,0);
		vector<int> v2(len,0);
		for(int j=0;j<len;j++) fscanf(fin,"%d",&(v1[j]));
		for(int j=0;j<len;j++) fscanf(fin,"%d",&(v2[j]));
		sort(v1.begin(),v1.end());
		sort(v2.rbegin(),v2.rend());
		result=0;
		for(int j=0;j<len;j++){
			result+=v1[j]*v2[j];
		}
		fprintf(fout,"Case #%d: %d\n",i+1,result);
	}
}
