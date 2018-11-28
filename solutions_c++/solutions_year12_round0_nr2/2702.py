#include <iostream>
using namespace std;

void GetMaxScore(int score, int *normal, int *suprise)
{
	int type = score % 3;
	int base = score / 3;
	if(type==0)
	{
		*normal  = base;
		if(base > 0)
			*suprise = base + 1;
		else
			*suprise = base;
	}else if(type==1)
	{
		*normal  = base + 1;
		*suprise = base + 1;
	}else if(type==2)
	{
		*normal  = base + 1;
		*suprise = base + 2;
	}
	return;
}

int GetMaxNumOfPeople(int N, int S, int P, int* score)
{
	int noPeople = 0;
	int noSuprise = 0;
	int normal = 0;
	int suprise = 0;
	for(int i=0;i<N;i++)
	{
		GetMaxScore(score[i], &normal, &suprise);
		if( suprise < P )
			continue;
		else if( normal >= P )
			noPeople++;
		else if(normal < P && suprise >= P && noSuprise < S)
		{
			noSuprise++;
			noPeople++;
		}
	}
	return noPeople;
}



int main()
{  
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small-out.txt","wt",stdout);

    int num = 0;
    cin >> num;
	int N, S, P;
	int score[100];

    for( int i=0; i<num; i++ )
    {
       cin >> N >> S >> P;
	   for( int j=0;j<N;j++)
		   cin >> score[j];   

	   cout << "Case #" << i+1 << ": " << GetMaxNumOfPeople(N, S, P, score) << endl;
    }
}