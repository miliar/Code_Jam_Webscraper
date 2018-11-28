/*
Google Codejam Round 1B
Prob Fix-it
By Phinfinity (anish)
*/
#include<cstdio>
#include<map>
#include<vector>
#include<cstring>
using namespace std;
class str
{
  public:
  char s[109];
  str()
  {
    s[0]='\0';
  }
  str(char *inp)
  {
    strcpy(s,inp);
  }
  void setstr(char inp[])
  {
    strcpy(s,inp);
  }
};
bool operator < (const str &a, const str &b)
{
  int i=0;
  while(a.s[i]==b.s[i] && a.s[i]!='\0')
    i++;
  return a.s[i]<b.s[i];
}

class dir
{
  public:
    map < str , dir* > m;
    vector <dir*> dirs;
    void adddir(str dirc,dir *&nowdir)
    {
      //printf("currently adding %s\n",dirc.s);
      dir *tmpd;
      tmpd = m[dirc];
      if(tmpd==NULL)
      {
	//printf("creating new entry\n");
	tmpd = new dir;
	m[dirc]=tmpd;
	dirs.push_back(tmpd);
      }
      //printf("dir addr %d\n",tmpd);
      nowdir = tmpd;
    }
};
void cleardirs(dir *cd)
{
      vector <dir*>::iterator it;
      for(it=cd->dirs.begin();it!=cd->dirs.end();it++)
	cleardirs(*it);
      cd->dirs.clear();
      cd->m.clear();
}
int tcnt;
void tabit()
{
  int i;
  for(i=1;i<=tcnt;i++)
    printf("\t");
}
int dircnt(dir *root)
{
  int ret,tmp;
  //tcnt++;
  ret=1;
  vector <dir*>::iterator it,endpt;
  endpt=(root->dirs).end();
    //tabit();
  //printf("in some dir\n");
  for(it=(root->dirs).begin();it!=endpt;it++)
  {
    tmp=dircnt(*it);
    //tabit();
    //printf("add %d\n",tmp);
    ret+=tmp;
  }
  //tabit();
  //printf("return %d\n",ret);
  //tcnt--;
  return ret;
}
int main()
{
  int t,ti,m,n,i;
  str tmps;
  char s[109],buf[109],*sp,*prevp;
  int fscnt,fincnt;
  dir root,*cdir;
  tcnt=0;
  scanf("%d",&t);
  for(ti=1;ti<=t;ti++)
  {
    cleardirs(&root);
    scanf("%d%d",&n,&m);
    for(i=1;i<=n;i++)
    {
      scanf("%s",s);
      sp=s;
      sp++;
      prevp=sp;
      cdir = &root;
      while(*sp)
      {
	if(*sp=='/')
	{
	  *sp='\0';
	  strcpy(buf,prevp);
	  tmps.setstr(buf);
	  cdir->adddir(tmps,cdir);
	  prevp=sp+1;
	}
	sp++;
      }
      strcpy(buf,prevp);
      tmps.setstr(buf);
      cdir->adddir(tmps,cdir);
    }
    fscnt=dircnt(&root);
    for(i=1;i<=m;i++)
    {
      scanf("%s",s);
      sp=s;
      sp++;
      prevp=sp;
      cdir = &root;
      while(*sp)
      {
	if(*sp=='/')
	{
	  *sp='\0';
	  strcpy(buf,prevp);
	  tmps.setstr(buf);
	  cdir->adddir(tmps,cdir);
	  prevp=sp+1;
	}
	sp++;
      }
      strcpy(buf,prevp);
      tmps.setstr(buf);
      cdir->adddir(tmps,cdir);
    }
    fincnt=dircnt(&root);
    //printf("ahem %d %d\n",fscnt,fincnt);
    printf("Case #%d: %d\n",ti,fincnt-fscnt);
  }
  return 0;
}