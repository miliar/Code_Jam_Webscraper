#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
	ofstream fout("A.out");
	int T,P,Q;
	cin>>T;
	int cnt;
	int i,j,k;
	int pos,c,ret,left,right;
	vector<int> tmp;
	//vector<int> v;
	for(i=0;i<T;++i)
	{
		cin>>P>>Q;
		vector<int> v(Q);
		for(j=0;j<Q;++j)
			cin>>v[j];
		sort(v.begin(),v.end());
		cnt=0;
		ret=10000000;
		do
		{
			++cnt;
			//vector<int> tmp;
			tmp.clear();
			tmp.push_back(v[0]);
			c=P-1;
			//ret=100000000;
			tmp.push_back(0);
			tmp.push_back(P+1);
			for(j=1;j<Q;++j)
			{
				tmp.push_back(v[j]);
				sort(tmp.begin(),tmp.end());
				bool found=false;
				for(k=0;k<tmp.size();++k)
					if(tmp[k]==v[j])
					{
						found=true;
						break;
					}
				if(!found)cout<<"Not found"<<endl;
				pos=k;
				//pos=find(tmp.begin(),tmp.end(),v[j]);
				//if(pos==0)left=0;
				left=tmp[pos-1];
				//if(pos==tmp.size()-1)right=P+1;
				right=tmp[pos+1];
			//	cout<<v[j]<<" "<<pos<<" "<<left<<" "<<right<<endl;
				/*if(v[j]>1)*/c+=v[j]-left-1;
				/*if(v[j]<P)*/c+=right-v[j]-1;
			}
			if(c<ret)
			{
			//	for(j=0;j<Q;++j)
			//		cout<<v[j]<<endl;
				ret=c;
			//	cout<<"cost: "<<ret<<endl;
			}
			
		}
		while(next_permutation(v.begin(),v.end()));
		//cout<<cnt<<" "<<Q<<endl;
		fout<<"Case #"<<(i+1)<<": "<<ret<<endl;
	}
	//ifstream fin("A.in");
	return 0;
}
