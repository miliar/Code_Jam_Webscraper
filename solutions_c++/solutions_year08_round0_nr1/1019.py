#include<cstdio>
#include<set>
#include<cstring>
using namespace std;
set<int> mS;
char names[101][110];
char smiec[20];
int S,Q;
int id[1000];
char my_in[110];
bool equals(int n){
    int lenA = strlen(names[n]),
	lenB = strlen(my_in);
    if(lenA == lenB){
	for(int i=0;i<lenA;i++)
	    if(names[n][i]!=my_in[i])
		return false;
	return true;
    }
    return false;
}
int main()
{
    int N;
    scanf("%d", &N);
    int cnt=0;
    while(N--){ cnt++; printf("Case #%d: ", cnt);
	scanf("%d", &S);
	fgets(my_in, 200, stdin);
	for(int i=0;i<S;i++)
	    fgets(names[i], 200, stdin);
	scanf("%d", &Q);
	fgets(my_in, 200, stdin);
	for(int i=0;i<Q;i++){
	    fgets(my_in, 200, stdin);
	    for(int j=0;j<S;j++)
		if(equals(j))
		    {id[i]=j; break;}
	}
	int nb=0;
	for(int i=0;i<Q;i++){
	    mS.insert(id[i]);
	    if(mS.size()==S){
		nb++;
		mS.clear();
	    }
	}
	printf("%d\n", nb);
    }
    return 0;
}
