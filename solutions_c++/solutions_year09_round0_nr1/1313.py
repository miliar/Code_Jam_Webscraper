#include <iostream>
#include <string.h>


using namespace std;
int sizeofWord;


class node
{
public:
  bool isOn;
  node *letters[26];
node()
  {
    for(int i=0;i<26;i++)
      letters[i]=NULL;
    isOn=true;
  }  
};

node *dict;



  void addWord(char word[])
  {
    node *temp1=dict;
    //cout<<"adding word   "<<word;
    for(int i=0;i<sizeofWord;i++)
      {
	if(temp1->letters[word[i]-'a']==NULL)
	  temp1->letters[word[i]-'a']=new node;
	temp1=temp1->letters[word[i]-'a'];
      }        
  }



bool isWord(char word[])
{
  node *temp=dict;
  int i;
  for( i=0;i<sizeofWord;i++)
    {
      if(temp->letters[word[i]-'a']==NULL)
	break;
      temp=temp->letters[word[i]-'a'];
    }
  return !(i<sizeofWord);
}





char pattern[1000];
int len;
int process(int i,node *tillNow,int already)
{
  int j,k,count=0;
  if(already==sizeofWord)
    return 1;
  if(i>=len)
    return 0;
  if(pattern[i]!='(')
    {
      if(tillNow->letters[pattern[i]-'a']==NULL)
	return 0;
      else
	return process(i+1,tillNow->letters[pattern[i]-'a'],already+1);
    }
  else
    {
      for(j=i;i<len&& pattern[j]!=')';j++);      //assuming the end is by ')' only..
      {
	k=j;
	for(j--;j>i;j--)
	  {
	     if(tillNow->letters[pattern[j]-'a']!=NULL)
	       count+= process(k+1,tillNow->letters[pattern[j]-'a'],already+1);
	  }
      }
    }
  return count;
}





int main()
{
  int noWords,noTestCases;
  cin>>sizeofWord>>noWords>>noTestCases;
  char word[50];

  dict=new node;
  for(int i=0;i<noWords;i++)
    {
      cin>>word;
      addWord(word);
    }
  for(int i=0;i<noTestCases;i++)
    {
      cin>>pattern;
      len=strlen(pattern);
	//cout<<"pattern   : "<<pattern<<endl;
      cout<<"Case #"<<i+1<<": "<<process(0,dict,0)<<endl;
    }
}
