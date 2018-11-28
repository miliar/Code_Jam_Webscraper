#include<iostream>

using namespace std;

int main(void)
{
	int tc, count=0;
	cin>>tc;
	while(tc--)
	{
		int D, C, size;
		cin>>C;
		string nons[C];
		for(int i=0; i<C; ++i)
			cin>>nons[i];
		cin>>D;
		string op[D];
		for(int i=0; i<D; ++i)
			cin>>op[i];
		
		string queue;
		cin>>size;
		cin>>queue;

		string result;
		for(int i=0; i<size; ++i)
		{
			result.push_back(queue[i]);
			int s = result.size();
			if(s>1){
				//check nons;
				for(int k=0; k<C; ++k){
					s = result.size();
					if(s<2) break;
					if(result[s-1] == nons[k][0])
					{
						if(result[s-2]==nons[k][1]){
							if(s==2) result.clear();
							else result.erase(s-2, s-1);
							result.push_back(nons[k][2]);
						}
					}
					else if(result[s-1] == nons[k][1])
					{
						if(result[s-2]==nons[k][0]){
							if(s==2) result.clear();
							else
								result.erase(s-2, s-1);
							result.push_back(nons[k][2]);
						}
					}
				}
				//check opposed;

				s = result.size();
				for(int k=0; k<D; ++k){
					if(result[s-1] == op[k][0])
					{
						for(int m=0; m<s; ++m)
							if(result[m]==op[k][1])
								result.clear();
					}
					else if(result[s-1] == op[k][1])
					{
						for(int m=0; m<s; ++m)
							if(result[m]==op[k][0])
								result.clear();
					}
				}
			}
		//	cout<<result<<endl;
		}
		cout<<"Case #"<<++count<<": ";
		int s = result.size();
		cout<<'[';
		for(int i=0; i< s-1; ++i)
			cout<<result[i]<<", ";

		if(s!=0)
			cout<<result[s-1]<<']'<<endl;
		else
			cout<<']'<<endl;
	}

	return 0;
}
