#include<iostream>


unsigned long long converttosmallest(const char *str,int length,int base)
{
    unsigned long long num=0;
    unsigned long long mul=1;
   // std::cout<<"digits="<<str<<"  Number"<<num<<std::endl;
    for (int i=length-1;i!=-1;i--)
    {
        if(str[i]>='0'&& str[i]<='9')
            num+=mul*(str[i]-'0');
        else
            num+=mul*(str[i]-'a'+10);
        mul*=base;
      // std::cout<<"Number"<<num<<"  Base"<<mul<<std::endl;
    }
    return num;
}

int main()
{
   int num;
   int count=1;
   std::cin>>num;
   char arr[36]={'1','0','2','3','4','5','6','7','8','9','a','b'
       ,'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
   while(num--)
   {
      std::string number,temp;
      std::cin>>number;
      temp=number;
      int k=0;
      for (int i=0;i<number.length();i++)
      {
          char rep=' ' ;
          if (number[i]!=' ')
          {
                rep=number[i];
            
          for (int j=i;j<number.length();j++)
          {
               if (number[j]==rep)
               {
                  temp[j]=arr[k];
                  number[j]=' ';
               }
          }
          k++;
          }
      }
      int base=k;
      if (base==1) base=2;     
      unsigned long long res=converttosmallest(temp.c_str(),temp.length(),base);
      
      std::cout<<"Case #"<<count++<<": "<<res<<std::endl;
   }


    return 0;
}
