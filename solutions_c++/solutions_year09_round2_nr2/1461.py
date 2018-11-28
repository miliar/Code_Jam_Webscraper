#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> Num;
static ofstream out("out.txt");


int Comp(const void *a, const void *b)
{
      return (int)(*(int *)a-*(int *)b);
}

void GetNum(int num)
{
      Num.clear();
      while(num)
      {
            Num.push_back(num%10);
            num/=10;
      }
}

void Cal(int num)
{
      int i,j,index;
      int size;
      int tmp,Min,k;
      int record[20];

      GetNum(num);
      size=Num.size();
      tmp=Num[0];
      for(i=1;i<size;++i)
      {
            if(Num[i]>=tmp)
            {
                  tmp=Num[i];
            }
            else
            {
                  index=0;
                  Min=10;
                  for(j=0;j<i;++j)
                  {
                        if(Num[j]>Num[i] && Num[j]<Min)
                        {
                              Min=Num[j];
                              k=j;
                        }
                  }
                  record[index]=Num[i];
                  for(j=0;j<i;++j)
                  {
                        if(j!=k)
                        {
                              record[++index]=Num[j];
                        }
                  }
                  qsort(record, index+1, sizeof(int), Comp);
                  break;
            }
      }
      if(i==size)
      {
            Min=10;
            for(i=0;i<size;++i)
            {
                  if(Num[i]!=0 && Num[i]<Min)
                  {
                        Min=Num[i];
                        k=i;
                  }
            }
            for(i=0,index=0;i<size;++i)
            {
                  if(i!=k)
                  {
                        record[index++]=Num[i];
                  }
            }
            qsort(record, index, sizeof(int), Comp);
            Num.clear();
            for(i=0;i<index;++i)
            {
                  Num.push_back(record[index-i-1]);
            }
            Num.push_back(0);
            Num.push_back(Min);
      }
      else
      {
            Num[i]=Min;
            for(j=0;j<i;++j)
            {
                  Num[j]=record[index-j];
            }
      }
      size=Num.size();
      for(i=size-1;i>=0;--i)
      {
            out << Num[i];
      }
      out << endl;
}

int main()
{
      int N;
      int num;
      int i;

      cin >> N;
      for(i=0;i<N;++i)
      {
            cin >> num;
            out << "Case #" << i+1 << ": ";
            Cal(num);
      }
      return 0;
}