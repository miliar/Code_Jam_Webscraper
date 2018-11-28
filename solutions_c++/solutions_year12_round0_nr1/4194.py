#include<iostream>
using namespace std;

int  main()
{
     char a1[100]=  "ejp mysljylc kd kxveddknmc re jsicpdrysi";
     char b1[100] = "our language is impossible to understand";
     char a2[100]=   "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
     char b2[100]= "there are twenty six factorial possibilities";
     char a3[100] ="de kr kd eoya kw aej tysr re ujdr lkgc jv";
     char b3[100]= "so it is okay if you want to just give up";
     
     int i =0,T,j;
     char alph[26],input[110];
     for(i =0 ; i < 26 ; i++)
     alph[i] = ' ';
     i =0;
     while(a1[i] != '\0')
     {           
                 if(a1[i] >= 97 && a1[i] <=122)
                 alph[a1[i]-97] = b1[i];
                 i++;
     } 
     
      i =0;
     while(a2[i] != '\0')
     {
                 if(a2[i] >= 97 && a2[i] <=122)
                 alph[a2[i]-97] = b2[i];
                 i++;
     }
     
      i =0;
     while(a3[i] != '\0')
     {
                 if(a3[i] >= 97 && a3[i] <=122)
                 alph[a3[i]-97] = b3[i];
                 i++;
     }
     
     alph['z' - 97] = 'q';
     alph['q' -97 ] ='z';
   
 /*  int p;  
 for(i = 0 ;i < 26; i++)
 cout <<alph[i] <<" " << i+1 << "\n";   
 cin >> p;*/
   cin >> T;
   i = 0;
   cin.getline(input,110,'\n');
   while(i < T)
   {
           cin.getline(input,110,'\n');
           j =0;
         //  cout << input << "\n";
           while(input[j] != '\0')
           {
                          if(input[j] >= 97 && input[j] <=122)
                          input[j] = alph[input[j] - 97];
                          j++;
           }
          // cout << input << "\n";
           cout <<"Case #" << i+1 << ": " << input << "\n";
           i++;
   }       
 return 0;         
}   










