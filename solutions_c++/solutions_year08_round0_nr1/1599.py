/*
	A. Saving the Universe problem
	Google Code Jam '08 - Qualification Round
	- n@p [ 17-Jul-2008 ]
	Note: This code was written and debugged on Borland's Turbo C++ version 3.0
*/

#include<stdio.h>
#include<string.h>
#include<conio.h>
#include<iostream.h>

#define S_MAX 100  //  10 for small
#define Q_MAX 1000 // 100 for small

#define S_NAME_MAX 100

char s[S_MAX][S_NAME_MAX+1], temp[S_NAME_MAX+1];
int q[Q_MAX];

int S, Q;

int findFirst(int id, int startPos)
{
	int pos;
	for(pos=startPos;pos<Q;pos++)
		if(q[pos]==id) return (pos-startPos);

	return -1; //in case its not in the list, it'll return -1
}

/*
void getstr(char *str)
{
	char *ptr;
	char t;
	do
	{
		cin.read(&t,1);
		*ptr=t;
		cout<<"\n"<<*ptr<<"\t"<<(int)(*ptr);
		ptr++;
	} while(t!='\n'||t!='\r');
	ptr--;
	*ptr='\0';
}

void tmain()
{
	char ham[80];
	int n; //char c;
	cin>>n; //cin>>c;
	cin.get(); cin.getline(ham,79);//getstr(ham); //cin.getline(ham,79);
	cout<<endl<<n<<"\t\'"<<ham<<"\'"<<endl;
}
*/

void main()
{
int n, m, i, cases, switches, f, max, maxS;
cin>>cases; //scanf("%d",&cases);
for(n=1;n<=cases;n++)
{
//printf("\n\n");

	//input search engines...
	cin>>S; //scanf("%d", &S);
	cin.get(); //gets(temp);
	//fflush(stdin);
	for(m=0;m<S;m++)
	{
		cin.getline(s[m], S_NAME_MAX); //gets(s[m]);
//printf("Search Engine #%d: \'%s\'\n", m, s[m]);
	}

	//input queries...
	cin>>Q; //scanf("%d", &Q);
	cin.get(); //gets(temp);
	//fflush(stdin);
	for(m=0;m<Q;m++)
	{
		cin.getline(temp,S_NAME_MAX); //gets(temp);
		q[m]=-1; //default,if the query is a non-search engine name
		for(i=0;i<S;i++)
			if(strcmp(temp, s[i])==0) q[m]=i;
//printf("Query #%d: %d [%s]\n", m, q[m], s[q[m]]);
	}

	//overall loop...
	switches=0;
	m=0;
	while(m<Q)
	{
		//search each engine name n find max dist..
		max=-1; maxS=-1;
		for(i=0;i<S;i++)
		{
			f=findFirst(i, m);
//printf("findFirst(%s,%d)=%d\n",s[i],m,f);
			if(f==-1) goto DONE;
			if(f>max)
			{
				max=f;
				maxS=i;
			}
		}
//printf("StartPos=%d; Max dist: %d [%s] at a dist of %d\n", m, maxS, s[maxS], max);
		switches++;
		m+=max;
	}

DONE:
	cout<<"Case #"<<n<<": "<<switches<<endl; //printf("Case #%d: %d\n", n, switches);
}

//printf("\nDone.\n");
//getch();
}