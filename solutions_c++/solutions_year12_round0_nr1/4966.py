#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

int A[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
    int t,i;
	char c;
    scanf("%d" , &t );
    c = getchar();
    char input[110] , output[110];
   
    int count = 0;
    while( t-- ){
           count++;
           i = 0;
           fflush( stdin );


           while( ( input[i] = getchar() ) != '\n' )
           {
                  if( input[i] == ' ' )
                             c = input[i];
                  else {
                       c = input[i];
                       c = c - 'a';
                      c = A[c];
                  }
                  output[i] = c;
                  i++;
           }
           output[i] = '\0';

           printf("Case #%d: %s\n" , count , output );
    }


    return 0;
}
















