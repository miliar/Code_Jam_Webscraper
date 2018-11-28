#include <iostream>
#include <vector>
using namespace std;

char s[1000100];
char word[5010][20];
vector <int> v[20][30];

int hash[6000];
bool vash[6000];
int L , D , N;

void Process(int len , int D)
{
	for (int i=0 ; i<20 ; i++){

		for (int j=0 ; j<30 ; j++){

			v[i][j].clear();
		}
	}

	for (int i=0 ; i<len ; i++){

		for (int j=0 ; j<D ; j++){

			v[i][word[j][i] - 'a'].push_back(j);
		}
	}
}

void Work(int st , int en , int id)
{
	int size , temp;
	memset(vash , 0 , sizeof(vash));
	for (int i=st ; i<=en ; i++){

		temp = s[i] - 'a';
		size = v[id][temp].size();
		for (int j=0 ; j<size ; j++){

			vash[v[id][temp][j]] = true;
		}
	}

	for (int i=0 ; i<D ; i++){

		if (vash[i])
			hash[i]++;
	}
}

int Cal()
{
	memset(hash , 0 , sizeof(hash));
	int len = strlen(s);
	int pos = 0 , ret = 0;
	int st , en;
	for (int i=0 ; i<len ; i++){

		if (s[i] == '('){

			st = i + 1;
			en = st;
			while (s[en] != ')' && en < len)
				en++;
			i = en;
			en--;
			Work(st , en , pos++);
		}
		else{

			st = i;
			en = i;
			Work(st , en , pos++);
		}
	}

	for (int i=0 ; i<D ; i++){

		if (hash[i] == L)
			ret++;
	}
	return ret;
}

int main()
{
	
//	freopen("A-large.in" , "r" , stdin);
//	freopen("A-large.out" , "w" , stdout);
	int ans;
	scanf("%d %d %d" , &L , &D ,&N);
	for (int i=0 ; i<D ; i++){

		scanf("%s" , word[i]);
	}
	Process(L , D);

	ans = 0;
	for (int i=0 ; i<N ; i++){

		scanf("%s" , s);
		ans = Cal();
		printf("Case #%d: %d\n" , i + 1 , ans);
	}
	return 0;
}