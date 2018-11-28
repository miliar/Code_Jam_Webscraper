#include <iostream>
#include<vector>
#include<string>

int main () 
{
  int L,D,N;
  std::cin>>L>>D>>N;
  std::vector<std::string> words(D);
  for (int i=0;i<D;i++)
  {
    std::cin>>words[i];
    //std::cout<<"Word -> "<<words[i]<<std::endl;
  } 
  std::string temp; 
 // std::vector< std::vector<char> > example(L);
  for (int i=0;i<N;i++)
  {
    std::vector<bool> wordSelected(D,1);
    std::cin>>temp;
    //std::cout<<"For -> "<<temp<<std::endl;
    for (int k=0,j=0;k<temp.length();k++,j++)
    {
        std::vector<bool> wordSel(D,0);
        if (temp[k]=='(')
        {
            k++;
            while(temp[k]!=')')
            {
               for (int x=0;x<D;x++)
               {
                   //std::cout<<"wordSelected[x]="<<wordSelected[x]<<"  temp[k]="<<temp[k]<<"   words[x][k]="<<words[x][j] <<std::endl;
                   if (wordSelected[x]&&temp[k]==words[x][j])
                   {
                       wordSel[x]=1;
                   }
               }
               //example[j].push_back(temp[k]);
               k++;
            }
    
        }
        else
        {
                          for (int x=0;x<D;x++)
               {

                   if (wordSelected[x]&&temp[k]==words[x][j])
                   {
                       wordSel[x]=1;
                   }
               }

           //example[j].push_back(temp[k]);
        }
       //  std::cout<<"Word Selected";
       // for (int z=0;z<D;z++)
       //     std::cout<<wordSel[z];
       // std::cout<<std::endl;
        wordSelected=wordSel;
    }
    int count=0;
    for (int k=0;k<D;k++)
    {
       if (wordSelected[k])
       {
           count++;
       }
    }
    std::cout<<"Case #"<<i+1<<": "<<count<<std::endl;
  }
  return 0;
}
