/* Enter your code here. Read input from STDIN. Print output to STDOUT */

#include<iostream>
#include<algorithm>
#include<math.h>
#include<map>
#include<algorithm>
using namespace std;

#define fr(i,a,b) for(i=(a);i<(b);++i)

int main()
    
    
{
int i,j,tt,k;
map<char ,char > m;
map<char , char >:: iterator mitr;
	freopen( "C:\\code_jam_io_files\\input.txt", "r", stdin );
	freopen( "C:\\code_jam_io_files\\output.txt", "w", stdout );

string s="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string t="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
for(i=0;i<s.length();i++)
  {
   if(s[i]==' ')
   continue;
   else                              
  m[s[i]]=t[i];
  } 
 
 m['q']='z';
 m['z']='q';
m[' ']=' ';

/*for(mitr=m.begin();mitr!=m.end();mitr++)
 {
   cout<<mitr->first<<" "<<mitr->second;
   
   cout<<"\n";
   
                                   
 }


cout<<m.size()<<"\n"; 
*/
char *line=(char *) malloc(105*sizeof(char));
char *result=(char *) malloc(105*sizeof(char));
scanf( "%d\n", &tt );
fr(i,0,tt)
 {
       printf( "Case #%d: ", i+1 );   
 gets(line);
 for(k=0;k<=strlen(line);k++)
    {
        result[k]=m[line[k]];                              
    }
 
 
  puts(result);
          
          
          
 
 
 
 }








return 0;
}
