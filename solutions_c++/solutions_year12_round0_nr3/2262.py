#include<iostream>
#include<stdlib.h>
#include<string>
#include<fstream>
#include<map>

using namespace std;

int main()
{
    int testcases;
    int min, max;
    char arr[100], brr[100], temp[100], remember[100][100];
    int count=0;
    int size;
    ifstream fin;
    ofstream fout;
    int i,j,k,l,m,n;

    fin.open("C-large.in", ios::in);
    fout.open("C-large.out", ios::out);
    
    fin>>testcases;
    
    for(i = 1; i<=testcases; i++)
    {
            count =0;
            fin>>min>>max;
            itoa(max, brr, 10);
            for(j=min; j<=max; j++)
            {
                    itoa(j, arr, 10);       
                    int len = strlen(arr)-1;
                    size=-1;
                    for(k=len; k>=0; k--)
                    {
                            if(arr[k] == '0')
                                 continue;
                            else if(arr[k] < arr[0])
                                 continue;
                            
                            for(m = k, n=0; n<=len ; m++, n++)
                            {
                                    temp[n] = arr[m];
                                    if(m==len)
                                              m=-1;
                            }
                            temp[n]='\0';
                
                            if(strcmp(temp,arr) <= 0 || strcmp(temp, brr) > 0)
                                                continue;
                                                
                            for(l=0; l<=size; l++)
                            {
                                    if(strcmp(temp, remember[l]) == 0)
                                                   break;
                            }
                            if(l <= size)
                                 continue;

                            size++;
                            strcpy(remember[size], temp);
                            count++;
                            
                    }
            }

            fout<<"Case #"<<i<<": "<<count<<endl;
    }
}
