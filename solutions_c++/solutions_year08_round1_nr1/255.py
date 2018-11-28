#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>

using namespace std;


char hex(int value)
{
  switch(value)
  {
    case 10:
      return 'a';
    case 11:
      return 'b';
    case 12:
      return 'c';
    case 13:
      return 'd';
    case 14:
      return 'e';
    case 15:
      return 'f';
    default:
      return (value+48);
  }
}

void sort1(vector<int> *list)
{
 for(int i=0;i<(*list).size();i++)
 {
  for(int j=i+1;j<(*list).size();j++)
  {
   if((*list)[j]<(*list)[i])
   {
    int temp;
    temp=(*list)[j];
    (*list)[j]=(*list)[i];
    (*list)[i]=temp;
   }
  }
 }
}

void sort2(vector<int> *list)
{
 for(int i=0;i<(*list).size();i++)
 {
  for(int j=i+1;j<(*list).size();j++)
  {
   if((*list)[j]>(*list)[i])
   {
    int temp;
    temp=(*list)[j];
    (*list)[j]=(*list)[i];
    (*list)[i]=temp;
   }
  }
 }
}

int main()
{

  FILE *f = fopen("A-small.in","r");
  int n;

  if(f==NULL)
    printf("no file");
  fscanf(f,"%d",&n);
  
  for(int i=0;i<n;i++)
  {
   vector<int> list1;
   vector<int> list2;
   int num;
   fscanf(f,"%d",&num);
   for(int j=0;j<num;j++)
   {
    int temp;
    fscanf(f,"%d",&temp);
    list1.push_back(temp);
   }
   sort1(&(list1));
   for(int j=0;j<num;j++)
   {
    int temp;
    fscanf(f,"%d",&temp);
    list2.push_back(temp);
   }
   sort2(&(list2));
   int sum=0;

   for(int j=0;j<num;j++)
   {
    sum+=list1[j]*list2[j];
   }

   FILE *fout=fopen("A-small.out","a");
   fprintf(fout,"Case #%d: %d\n",(i+1),sum);
   fclose(fout);
  }

  fclose(f);
}
