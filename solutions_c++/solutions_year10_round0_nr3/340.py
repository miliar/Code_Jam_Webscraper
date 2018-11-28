#include<iostream>
using namespace std;


// R : nombre de fois par jour < 10^8
// k : nombre de personne dans le wagon
// N :nombre de groupes < 1000
// T : nombre de tests < 50
//
int somme[1000];
int prochain[1000];
int groupes[1000];
int main()
{
int T;
int R,k,N;
cin >> T;
for(int cas = 1 ; cas <= T ; cas++)
{	
	cin >> R >> k >> N ;
	for(int i=0; i< N ; i++)
		cin >> groupes[i];
	for(int i =0 ; i<N ; i++)
	{	
		int charge = 0;
		int j=0;
		for(; charge <= k && (j <= N); j++)
			charge+=groupes[(i+j) % N ];
		j--;
		somme[i] = charge - groupes[(i+j) % N];
		//cout << "j= " << j << " et somme[" << i << "] = " <<somme[i] << " " ;
	        prochain[i]=(i+j)%N;	
	}
	long long int recette = 0;
	int grp = 0; 
	for( int i = 0 ; i<R ; i++)
	{
		recette += somme[grp];
		grp = prochain[grp];
	}
	cout << "Case #" << cas << ": " << recette << endl;
}
return 0;
}
