#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
int main()
{
    int num;
    std::cin>>num;
     int case1=1;
    while(num--)
    {
        std::cout<<"Case #"<<case1++<<": ";
        std::string temp;
        std::cin>>temp;
        std::vector<int> list;int i;
        if (temp.length()==1) list.push_back(temp[0]-'0');
        for ( i=temp.length()-1;i!=0;i--)
        {
            if (temp[i]>temp[i-1])
            {
               list.push_back(temp[i]-'0');
               break;
            }else
            list.push_back(temp[i]-'0');
            if (i==1) list.push_back(temp[0]-'0');
        }
        std::sort(list.begin(),list.end()); 
       //std::cout<<"begin list "<<std::endl;
       // for(int y=0;y<list.size();y++){std::cout<<list[y];}std::cout<<std::endl;
       //std::cout<<"\nValue of i="<<i<<std::endl;
       if (i!=0)
       {
        for (int z=0;z<i-1;z++)
           std::cout<<temp[z];
        for(int y=0;y<list.size();y++)
            if(temp[i-1]-'0'<list[y]){ std::cout<<list[y];list[y]=temp[i-1]-'0';
             break;}
       for(int y=0;y<list.size();y++)std::cout<<list[y];
       }else
       {int l=-1;
      // std::cout<<list[0]<<'0';
       for(int y=0;y<list.size();y++){if (list[y]!=0){
          std::cout<<list[y]<<'0';l=y;break;}}
       for(int y=0;y<list.size();y++){if (l==y) continue;
          std::cout<<list[y];}
       }
        std::cout<<std::endl;
    }
}
