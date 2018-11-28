#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
struct edge
{
	char ch ;
	int i;
}q[5010];
string s[5010],ss[1000];
int num = 0 , n , m , k ; 
bool cmp( edge w,edge e) {return w.ch<e.ch;}
int search(char c)
{
	int l=0,r=m;
	while(l<=r)
	{
		int mid=(l+r)/2;
		if(q[mid].ch==c)
		{
			return mid;
		}
		else if ( q[mid].ch>c) r=mid-1;
		else l=mid+1;
	}
	return -1;
}
int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,e,ee,r;
	char ch[1000];
	scanf("%d%d%d",&n,&m,&k);
	getchar();
	for ( i = 0 ;i < m ;i ++ ) {scanf("%s",ch);s[i]=ch;}
	for ( i = 0 ; i < m ;i ++ ) {q[i].ch=s[i][0];q[i].i=i;}
	sort(q,q+m,cmp);
//	for ( i = 0 ;i < m ;i ++ ) cout<<q[i].ch<<' '<<q[i].i<<endl;
	for ( i = 0 ;i < k ;i ++ ) 
	{
		int scr = 0 ; 
		num = 0 ;
		scanf("%s",ch);
		int l=strlen(ch);
		for ( j = 0 ; j < l; j ++ ) 
		{
			if ( ch[j]!='(') {ss[num++]+=ch[j];continue;}
			for (  r =j ; r < l; r ++ ) 
			{
				if ( ch[r] == ')' ) break ;
				if ( ch[r] == '(' ) continue ;
				ss[num]+=ch[r];
			}
			j=r;
			num++;
		}
	//	for ( j = 0 ; j < num ; j ++ ) cout<<ss[j]<<endl;
		for ( j = 0 ;j < ss[0].length(); j ++ ) 
		{
			int t=search(ss[0][j]);
			if(t==-1) continue;
			for ( r = t;r>=0;r--)
			{
				if(q[r].ch!=ss[0][j]) break;
				for ( e = 1 ; e < s[q[r].i].length() ; e ++ ) 
				{
					for ( ee = 0 ; ee < ss[e].length(); ee++)
					{
						if( ss[e][ee]==s[q[r].i][e] ) break;
					}
					if ( ee == ss[e].length()  ) break ; 
				}
				if( e == num ) scr ++;
			}
			for ( r = t+1;r<m;r++)
			{
				if(q[r].ch!=ss[0][j]) break;
				for ( e = 1 ; e < s[q[r].i].length() ; e ++ ) 
				{
		     		for ( ee = 0 ; ee < ss[e].length(); ee++)
					{
						if( ss[e][ee]==s[q[r].i][e] ) break;
					}
					if ( ee == ss[e].length()  ) break ; 
				}
				if( e == num ) scr ++;
			}
		}
		printf("Case #%d: %d\n",i+1,scr);
		for ( j = 0 ;j < num ; j ++ ) ss[j]="";
	}
	
	return 0;
}