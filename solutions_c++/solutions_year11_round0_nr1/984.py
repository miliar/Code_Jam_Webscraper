#include <cstdio>
#include <vector>

using namespace std;

struct press{
	int button;
	int place;
}temp;

vector<press> Orange;
vector<press> Blue;

int main()
{
	int T;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int z = 0; z < T; z++){
		Blue.clear();
		Orange.clear();
		int posO = 1;
		int posB = 1;
		int N;
		scanf("%d",&N);
		for(int i = 0; i < N; i++){
			char c1,c2,c3;
			scanf("%c%c%c",&c1,&c2,&c3);
			int num;
			scanf("%d",&num);
			temp.button = num;
			temp.place = i;
			if(c2=='O')
				Orange.push_back(temp);
			else
				Blue.push_back(temp);
		}

		temp.button = 1000;
		temp.place = 1000;
		Orange.push_back(temp);
		Blue.push_back(temp);

		int k = 0;
		int currentPos = 0;
		int O = 0;
		int B = 0;
		while(currentPos!=N){
			k++;
			if(currentPos==Orange[O].place && posO==Orange[O].button)
			{
				currentPos++;
				O++;
				if(Blue[B].button<posB)
					posB--;
				else if(Blue[B].button>posB)
					posB++;
			}
			else if(currentPos==Blue[B].place && posB==Blue[B].button){
				currentPos++;
				B++;
				if(Orange[O].button<posO)
					posO--;
				else if(Orange[O].button>posO)
					posO++;
			}
			else{
				if(Orange[O].button<posO)
					posO--;
				else if(Orange[O].button>posO)
					posO++;
				if(Blue[B].button<posB)
					posB--;
				else if(Blue[B].button>posB)
					posB++;
			}
		}
		printf("Case #%d: %d\n",z+1,k);
	}
	return 0;
}