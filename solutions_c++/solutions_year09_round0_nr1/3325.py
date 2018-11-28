#include<iostream>
using namespace std;
#include<string.h>



int main()
{
	//clrscr();
   char str[1000][1000],pattern[1000][1000];
   int L,N,D;
   int i,j=0,k,flag=0,cnt=0,word_count=0;
   //cout<<"enter length"<<endl;
   cin>>L;
   //cout<<"enter the no of words"<<endl;
   cin>>D;
    //cout<<"enter the no of patterns"<<endl;
    cin>>N;
    //cout<<"enter the words"<<endl;
    for(i=0;i<D;i++)
    for(j=0;j<L;j++)
    cin>>str[i][j];
    j=0;
    //cout<<"enter the patterns"<<endl;
    for(i=0;i<N;i++){
    scanf("%s",&pattern[i]);
    }
    //for(i=0;i<N;i++)
    //cout<<pattern[i]<<endl;
    int p;
    for(j=0;j<N;j++)
    {
	for(k=0;k<D;k++)
	{
	    i=0;
	    p=0;
	    while(pattern[j][i]){
	    //ca'cout<<pattern[j][i];
	   // if(pattern[j][i]==' ') i++;
	   //while(pattern[j][i]!='(') i++;
    if(pattern[j][i]=='(')
    {
		while(pattern[j][i]!=')')
		{


		    if(pattern[j][i]==str[k][p]){
		     //   cout<<pattern[j][i];
		    cnt++;
		    }
		    i++;
		}


    }
    else
    {
	    if(pattern[j][i]==str[k][p]){
	       // cout<<pattern[j][i];
	         cnt++;
	    }
    }
i++;
p++;
}

//cout<<" strlen"<<strlen(str[k])<<endl;
//cout<<" cnt:"<<cnt<<endl;

if(cnt==strlen(str[k]))
{
	word_count++;

}
cnt=0;
}

cout<<"Case #"<<j+1<<": "<<word_count<<endl;
word_count=0;
}

	return 0;
}

