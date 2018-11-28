
#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;


int  main()
{
	int N;
	//ifstream in("A-small.in");
	//ofstream out("A-small.out");
	//ifstream in("A-large.in");
	//ofstream out("A-large.out");
	
	//cin>>N;
	//in>>N;
	freopen("B-small-attempt0.in", "r", stdin); 
    freopen("2.txt", "w", stdout); 
	scanf("%d",&N);
	vector<int> v1start,v1end,v2start,v2end;
	
	int n=0;
	int tour;
	int num1,num2;
	int i,j;
	int total1,total2;
	int a,b,c,d;
	
	while(n++<N)
	{
		//cin>>tour;
		//in>>tour;
		scanf("%d",&tour);
		//cin>>num1>>num2;
		//in>>num1>>num2;
		scanf("%d %d",&num1,&num2);
		
		for(i=0;i<num1;i++)
		{
			scanf("%d:%d %d:%d",&a,&b,&c,&d);//cin>>start>>end;
			//printf("%d %d  %d %d",a,b,c,d);
		    v1start.push_back(a*100+b);//*100
		    v1end.push_back(c*100+d+tour);
		}
		
		for(i=0;i<num2;i++)
		{
			scanf("%d:%d %d:%d",&a,&b,&c,&d);
			//printf("%d %d  %d %d",a,b,c,d);
		    v2start.push_back(a*100+b);
		    v2end.push_back(c*100+d+tour);
		}
		
		sort(v1start.begin(),v1start.end());
		sort(v2end.begin(),v2end.end());
		total1=0;
		for(i=0,j=0;i<num1&&j<num2;)
		{
			if(v1start[i]<v2end[j])
			{
				total1++;
				i++;
			}else
			{
				i++;
				j++;
			}
			
		}
		
		total1+=num1-i;
		sort(v2start.begin(),v2start.end());
		sort(v1end.begin(),v1end.end());
		
		/*for(vector<int>::const_iterator it=v1start.begin();it!=v1start.end();it++)
		cout<<*it<<endl;
		
		for(vector<int>::const_iterator it=v2end.begin();it!=v2end.end();it++)
		cout<<*it<<endl;*/
		
		
		total2=0;
		for(i=0,j=0;i<num2&&j<num1;)
		{
			if(v2start[i]<v1end[j])
			{
				total2++;
				i++;
			}else
			{
				i++;
				j++;
			}
			
			
		}
		total2+=num2-i;
		//cout<<"Case #"<<n<<": "<<total1<<" "<<total2<<endl;
		printf("Case #%d: %d %d\n",n,total1,total2);
		v1start.clear();
		v1end.clear();
		v2start.clear();
		v2end.clear();
		

	}

}