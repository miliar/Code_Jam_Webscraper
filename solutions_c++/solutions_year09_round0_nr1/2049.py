#include <iostream>
using namespace std;

int main()
{

  int i,ii,ik;
  int count=0;
  int position=0;
  int l,d,n;
  char dictionary[5050][20];
  char s[1000];
  int ans=0;
  
  cin>>l>>d>>n;
  for (i=0;i<d;i++)
  {
    cin>>dictionary[i];
  }
  for (i=0;i<n;i++)
  {
    ans=0;
	count=0;
	position=0;
    cin>>s;
    bool map[20][30];
	for (ik=0;ik<16;ik++)
	{
	  for (ii=0;ii<26;ii++)
	  {
	    map[ik][ii]=false;
	  }
	}
	ii=0;
	while (ii<strlen(s))
	{
	  if (s[ii]=='(')
	  {
	    count++;
	  }
	  else if (s[ii]==')')
	  {
	    count--;
		position++;
	  }
	  else
	  {
	    map[position][s[ii]-'a']=true;
	    if (count==0)
		{
		  position++;
		}
	  }
	  ii++;
	}
	
	for (ik=0;ik<d;ik++)
	{
	  bool flag = true;
	  for (ii=0;ii<strlen(dictionary[ik]);ii++)
	  {
		if (!map[ii][dictionary[ik][ii]-'a'])
		{
		  flag = false;
		}
	  }
	  if (flag)
	  {
	    ans++;
	  }
	}
	cout<<"Case #"<<i+1<<": "<<ans<<endl;
  }

  return 0;
}