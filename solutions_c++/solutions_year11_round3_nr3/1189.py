#include <cstdlib>
#include <iostream>
#include <map>
#include <string>

using namespace std;

int p[110];
void work(){
	int i,j,k;
	
	int N,L,H;
	cin>>N>>L>>H;

	for (i=0; i<N; i++)
	{
		cin>>p[i];
	}

	bool done = false;
	for (i=L; i<=H; i++)
	{
		if(i==1) { done =  true; break;}
		for (j=0; j<N; j++)
		{
			if(p[j]>i){
				if(p[j] % i == 0){}
				else break;
			}else{
				if(i % p[j]== 0){}
				else break;
			}
		}
		if(j == N){
			done = true;
			break;
		}
	}
	if(done){
		cout<<i<<endl;
	}else{
		cout<<"NO\n";
	}
}

int main()
{
	freopen("C-small-attempt2.in" , "r" , stdin);
	freopen("C-small-attempt2.in.out" , "w" , stdout);

	int T;   
	cin>>T;

	for(int caseID = 1 ; caseID <= T ; caseID ++){
		cout<<"Case #"<<caseID<<": "; 
		work();
	}

	// system("PAUSE");
	return 0;
}