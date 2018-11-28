#include <iostream>

using namespace std;

int main()
{
	//cout << "Hello!!!" << endl;
	//return 0;
	int T, res;

	cin >> T;
	for(int t=1; t<=T; t++){
		/************************************
		*	Input Data
		*************************************/
		int N, NB=0, NO=0;
		int B[100], O[100];
		char name[100];
		cin >> N;
		for(int i=0; i<N; i++)
		{
			char c;
			cin >> c; name[i]=c;
			if(c=='B')
				cin >> B[NB++];
			else
				cin >> O[NO++];
		}
		/*for(int i=0;i<NB;i++)
			cout << B[i] << endl;
			*/
		/************************************
		*	Solve the Problem
		*************************************/
		res=0;
		int iB=0, iO=0, i=0, posB=1, posO=1;
		for(int i=0; i<N; i++)
		{
			int d;
			switch(name[i])
			{
				case 'B':	
							d=abs(posB-B[iB])+1; 		posB=B[iB++];
							if(abs(posO-O[iO])<=d)
								posO=O[iO];
							else
								posO=O[iO]+abs(posO-O[iO])-d;
							break;
				case 'O': 
							d=abs(posO-O[iO])+1; 		posO=O[iO++];
							if(abs(posB-B[iB])<=d)
								posB=B[iB];
							else
								posB=B[iB]+abs(posB-B[iB])-d;
							break;
			}
			res+=d;
		}
		/************************************
		*	Output Results
		*************************************/
		cout << "Case #" << t << ": " << res << endl;
	}

	return 0;
}
