#include <stdio.h>
#include <string.h>
#define EN 10
#define QR 100
#define C1 17
#define C2 43
#define cls(x) memset(x,0,sizeof(x))
const int N= 124287;
struct node
{
  char word[60];
  int l;
  int qed;
  struct node* next;
};
node *ht[N],buf[N];
node *hte[N],bufe[N];
int tten;
int n,m,pt=0,pte=0,ans,ct;

void init(node *ht[], node buf[], int &pt)
{
	int i;
	for (i=0;i<pt;i++)
	{
		ht[i]=NULL;
		buf[i].l=0;
		buf[i].qed=0;
		memset(buf[i].word,0,sizeof(buf[i].word));
	}
	pt=0;
};

int hash(char* p)
{
  unsigned s,g;

  s=0;
  while (*p) {
    s=(s<<4)+*p++;
    g=s&0xf0000000;
    if (g) s^=g>>24;
    s&=~g;
  }
  return s%N;
}

int insert(char* s,node *ht[],node buf[],int &pt)
{
  int h,i=0;
  struct node* p;
  h=hash(s);
  p=ht[h];
  while (p) {
    if (strcmp(s,p->word)==0)  
	{
		p->l++;
		return p->l;
	}
	i++;
    h=(h+i*C1+i*i*C2)%N;
	p=ht[h];
  }
  strcpy(buf[pt].word,s);
  buf[pt].l=1;
  buf[pt].next=ht[h];
  ht[h]=buf+pt;
  pt++;
  return 1;
}

int find(char* s,node *ht[], node buf[])
{
  struct node* p;
	int i=0;
	int h=hash(s);
  p=ht[h];
  while (p) {
	  if (strcmp(p->word,s)==0) return p->l;
    i++;
    h=(h+i*C1+i*i*C2)%N;
	p=ht[h];
  }
  return 0;
}

int qu(char* s,node *ht[], node buf[])
{
  struct node* p;
	int i=0;
	int h=hash(s);
  p=ht[h];
  while (p) {
	  if (strcmp(p->word,s)==0) 
	  {
		  p->qed++;
		  return p->qed;
	  }
    i++;
    h=(h+i*C1+i*i*C2)%N;
	p=ht[h];
  }
  return 0;
}

char eng[100];
char qur[QR][100];
void solve(int bg,char last[])
{
	int i,j,k,t,lastest,enct=0;
	lastest=-1;
	init(ht,buf,pt);
	if (strlen(last)) 
	{
		qu(last,hte,bufe);
		enct++;
	}
	for (i=bg;i<ct;i++)
		{
			if (qu(qur[i],hte,bufe)==1) enct++;
				k=insert(qur[i],ht,buf,pt);
				if (k==1&&strcmp(qur[i],last))
					lastest=i;
		}
	for (i=0;i<pte;i++) bufe[i].qed=0;
	if (enct==pte)
	{
		ans++;
		if (lastest+1<ct) solve(lastest+1,qur[lastest]);
	}
}
int main()
{
	int i,j,t,o,k;
	//freopen("df.out","w",stdout);
	scanf("%d",&t);
	for (o=1;o<=t;o++)
	{
		init(hte,bufe,pte);
		scanf("%d",&n);while(getchar()!='\n');
		ct=0;
		tten=0;
		for (i=0;i<n;i++)
		{
			gets(eng);
			insert(eng,hte,bufe,pte);
		}
		scanf("%d",&m);while(getchar()!='\n');
		for (i=0;i<m;i++)
		{
			gets(qur[ct]);
			if (find(qur[ct],hte,bufe)) ct++;
		}
		ans=0;
		solve(0,"");
		printf("Case #%d: %d\n",o,ans);
	}
	//fclose(stdout);
	return 0;
}
