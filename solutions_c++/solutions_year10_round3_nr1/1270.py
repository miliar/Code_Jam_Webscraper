//#include <algorithm>
//#include <iostream>
//using namespace std;
//
//
//struct Wire{
//	int left;
//	int right;
//};
//
//Wire all[1020];
//
//int cmp(Wire a,Wire b)
//{
//	return a.left>b.left;
//}
//
//
//int sum[10100];
//int main()
//{
//	int t,cases=0;
//
//	int n;
//	int i,j;
//	cin>>t;
//	while(t--)
//	{
//        memset(sum,0,sizeof(sum));
//		
//        cin>>n;
//		for(i=0;i<n;i++)
//		{
//			cin>>all[i].left>>all[i].right;
//			sum[all[i].right]++;
//		}
//
//		sort(all,all+n,cmp);
//
//		for(i=10010;i>=0;i--)
//		{
//			sum[i]=sum[i+1]+sum[i];
//		}
//
//		int ans=0;
//
//		for(i=0;i<n;i++)
//		{
//			ans+=sum[all[i].right+1];
//		}
//        printf("Case #%d: %d\n",++cases,ans);
//	}
//	return 0;
//}

#include<iostream>
#include<algorithm>
using namespace std;

struct city{
	int from;
	int to;
};

city citys[10000110];
int n;

int  C[100100];


//排序函数
int cmp(city a,city b)
{
	 return a.from > b.from;
}
//=================================


 int lowbit(int x)
{
    return x&(-x);
}

 int  sum(int i)
{
    int temp=0;
	while(i>0)
	{
	    temp+=C[i];
		i -= lowbit(i);
	}
	return temp;
}

void plus(int k,int data)  //在第k位置加上data
{
    while(k<=10010)
	{
	    C[k]+=data;
		k+=lowbit(k);
	}
}

//=================================
int main()
{
	int i,j,ii;
	int t;
	scanf("%d",&t);
	for(ii=1;ii<=t;ii++)
	{
        scanf("%d",&n);
        for(i=0;i<n;i++)
			scanf("%d%d",&citys[i].from,&citys[i].to);
        memset(C,0,sizeof(C));
		sort(citys,citys+n,cmp);
        
		//for(i=0;i<n;i++)
		//	cout<<citys[i].from<<" "<<citys[i].to<<endl;
        int res=0;
		for(i=0;i<n;i++)
		{
		     res += sum(citys[i].to-1);
			 plus(citys[i].to,1);

			 //cout<<n<<":";
			 //for(j=0;j<11;j++)
				// cout<<C[j]<<" ";
			 //cout<<endl;
		}

		printf("Case #%d: %d\n",ii,res);
	}
    return 0;
}