#include<iostream>
#include<string>
#include<algorithm>
#include<cstring>
#include<stdio.h>

using namespace std;
bool flag[5001];
char sample[16],store[16][30];
char dict[5001][16];

int main()
{
    bool mark;
    int L,D,N;
    int i,j,k,itr,I;
    cin >> L >> D >> N ;
    for ( i = 1 ; i <= D ; i++)
        cin >> dict[i] ;
    int array[30];

    int count = 0;
    char temp;
    for ( i = 1 ; i <= N ; i++ )
    {
        memset(flag,0,5001);
//         cout << "i = " << i << endl;
        count = 0 ;
        while(count < L ){
            cin >> temp;
            sample[count]='@';
            if ( temp!='('){
                sample[count] = temp ; 
            }
            else if ( temp=='(')
            {
                k = 0 ;
                cin >> temp ;
                while(temp!=')'){
                    store[count][k++]=temp;
                    cin >> temp ;
                }
                store[count][k]='\0';
            }
            count++;
        }
        sample[count] = '\0';
//         cout << sample << endl;
//         for(j=0;j<strlen(sample);j++)
//             cout << store[j] << endl;
        
        for( itr = 1 ; itr <= D; itr ++)
        {
/*            cout << dict[itr] << endl;*/
            for(j=0;j<strlen(sample);j++)
            {
                flag[itr]=1;
                if( sample[j] != dict[itr][j] && sample[j]!='@' ) { 
//                     cout << sample[j] << ' ' << dict[itr][j] << endl;
                    flag[itr] = 0; 
                    break;}
            }
        }
        for( itr = 1 ; itr <= D  ; itr ++)
        {
            if(flag[itr] == 1)
            {
//                 cout << sample << " " << dict[itr] << endl ;
                mark = 1;
                for( j = 0 ; j < strlen(sample) ; j++)
                {
                    if(sample[j] == '@' )
                    {
//                         cout << store[j] << endl;
                        mark = 0;
                        for( I = 0 ; I < strlen(store[j]) ; I ++)
                        {
//                             cout << dict[itr][j] << ' ' << store[j][I] << endl;
                            if(dict[itr][j] == store[j][I] ) 
                            {    mark = 1; }     
                        }
                        if(!mark) break;
                    }
                }
                if(!mark) flag[itr] = 0;
            }
        }
//         for( itr = 1 ; itr <= D; itr ++)
//             cout << flag[itr] << endl;
        count = 0;
        for( itr = 1 ; itr <= D ; itr ++){if (flag[itr] == 1 ) count++ ;}
        array[i] = count;
    }
    for(i=1;i<=N;i++)
    cout <<"Case #"<< i <<": " << array[i] << endl;
    return 0;
}