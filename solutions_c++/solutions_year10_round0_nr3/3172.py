#include <vector>
#include <numeric>
#include <iostream>

using namespace std;

long long add(int a,int b,vector<long long> vec){
	long long sum=0;//printf("gg%d%d",b,a);
	if(b>=a){
		for(int i=a;i<=b;i++){
			sum+=vec[i];
		}
	}
	return sum;
}
int main()
{
	freopen("data1.txt","r",stdin);
	int t;
	scanf("%d",&t);

	freopen("out1.txt","w",stdout);

	for(int m=1;m<=t;m++){
		long long r,k,n;

		scanf("%lld",&r);
        scanf("%lld",&k);
        scanf("%lld",&n);

		vector<int> q;

		for(int i=0;i<n;i++){
			int temp;
			scanf("%d",&temp);

			q.push_back(temp);
		}

		long long count=0;
		int counter=0,flag=0;
		
		vector<long long> aa;//long long
		vector<int> index;
		long long sum=0,j=0;
		
		int flag1=1;
		
		for(int i=0;i<q.size();i++){
			counter=0;
			if(i>0){
	            for(int g=0;g<index.size();g++){
					if(index[g]==j){
						flag1=0;
						break;
					}
				}
				if(flag1==0)break;
			}
			index.push_back(j);
			
			while((sum+q[j])<=k && counter<q.size()){
				sum+=q[j];
				j++;
				if(j==q.size())j=0;
				counter++;
			}
			if(counter==q.size()){
				flag=1;
			}
				aa.push_back(sum);
              //  printf("dd%d %d\n",sum,j);

				sum=0;

		}

		if(j==q.size())j=0;
	//	printf("dd%d",j);
		int want=0;
		for(int i=0;i<index.size();i++){
			if(index[i]==j){
				want=i;
				break;
			}
		}

		if(flag==1){
			count=add(0,aa.size()-1,aa)*r;//aa.begin(),aa.end(),0)*r;
		}else if(r<aa.size()){
			count=accumulate(aa.begin(),aa.begin()+r,0);
		}else{
			/*count=accumulate(aa.begin(),aa.begin()+want,0);printf("hello%d",aa.size());
			count+=accumulate(aa.begin()+want,aa.end(),0)*((r-want)/(aa.size()-want));printf("hello%lld",count);
			count+=accumulate(aa.begin()+want,aa.begin()+want+((r-want)%(aa.size()-want)),0);*/
			count=add(0,0+want-1,aa);//printf("hello%d",count);
            count+=add(0+want,aa.size()-1,aa)*((r-want)/(aa.size()-want));//printf("hello%d",count);
            count+=add(0+want,0+want+((r-want)%(aa.size()-want))-1,aa);
		}
		printf("Case #%d: %lld\n",m,count);

	}
	fclose(stdin);
	fclose(stdout);


	return 0;
}
