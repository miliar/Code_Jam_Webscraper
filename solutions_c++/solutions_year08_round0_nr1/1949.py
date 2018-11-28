#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main()
{
	int cases;
	vector<string> e,q;
	int ne,nq,k,i,j,max,maxe,cnt,caseno=1;
	string str;
    char buf[10000];	
	
	cin>>cases;

	while(cases--)
	{

		cin>>ne;
		cin.getline(buf,sizeof(buf));
		e.clear();

		for(i=0;i<ne;i++)
		{
    		cin.getline(buf,sizeof(buf));
    		str = string(buf);
			e.push_back(str);
		}

		cin>>nq;
        cin.getline(buf,sizeof(buf));
        str = string(buf);
		q.clear();

		for(i=0;i<nq;i++)
		{
			cin.getline(buf,sizeof(buf));
			str = string(buf);
            q.push_back(str);
		}


                if(nq==0) { cout<<"Case #"<<caseno++<<+": 0"<<endl; continue; }
		
		
		i=0;
		cnt=-1;
		
		while(i<nq)
		{
			cnt++;
			max=i;
			maxe=-1;
			for(k=0;k<ne;k++)
			{
				for(j=i;j<nq;j++)
					if(q[j]==e[k]) break;
				if(j>max) { max=j; maxe=k; }
			}
			i=max;
		}
		cout<<"Case #"<<caseno++<<": "<<cnt<<endl;
	}
	return 0;
}	
