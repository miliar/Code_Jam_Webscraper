
#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std ;

FILE *in = fopen("hold.in", "r") ;
FILE *out = fopen("hold.out", "w") ;


string intToStr(int n)
{
	int i,j;
	string str;

	if(n==0) return "0" ;
	str.resize(0);

	while( n!=0 )
	{
		str += (n%10 + '0')  ;
		n /= 10;
	}

	for(i=0,j=str.size()-1;i<str.size()/2;i++,j--)
		swap(str[i],str[j]);

	return str;
}





int strToInt(string str)
{
	int i,n,p;

	n = 0;
	p = 1;

	for(i=str.size()-1;i>=0;i--,p*=10)
		n += (str[i]-'0') * p ;

	return n;
}


int main()
{
    int i, j, k, l ;
    int A, B, h, ans ;
    string str ;
    int g, t ;
    vector <int> hold ;

    fscanf(in, "%d", &k) ;
    for(l=1;l<=k;l++)
    {
        fscanf(in, "%d%d", &A, &B) ;
        ans = 0 ;
        for(i=A;i<=B;i++)
        {
            str = intToStr(i) ;
            g = str.size() ;
            hold.clear() ;
            for(j=0;j<g;j++)
            {
                str = str[str.size()-1] + str.substr(0, str.size()-1) ;
                h = strToInt(str) ;
                if( h != i && i < h && h <= B && h > A && i >= A && i < B && str[0] != '0')
                {
                    for(t=0;t<hold.size();t++)
                        if( hold[t] == h ) break ;
                    if( t == hold.size() )
                    {
                        hold.push_back(h) ;
                        ans ++ ;
                    }
                    //if( l == 4 ) fprintf(out, "%d --- %d\n", i, h) ;
                }
            }
        }
        fprintf(out, "Case #%d: %d\n", l, ans) ;
    }


    return 0 ;
}
