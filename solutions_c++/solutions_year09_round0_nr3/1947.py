#include<stdio.h>
#include<iostream>
#include<fstream>
#include<vector>
#include<ctype.h>


using namespace std;

int count;
vector<int> buckets[20];
void push_into_bucket(int val,char bucket_id)
{
     switch(bucket_id)
     {
                      case 'w':
                           {
                               buckets[0].push_back(val);
                               break;
                           }
                      case 'e':
                           {
                               buckets[6].push_back(val);
                               buckets[1].push_back(val);
                               buckets[14].push_back(val);
                               break;
                           }
                      case 'l':
                           {
                               buckets[2].push_back(val);
                               break;
                           }
                      case 'c':
                           {
                               buckets[3].push_back(val);
                               buckets[11].push_back(val);
                               break;
                           }
                      case 'o':
                           {
                               buckets[4].push_back(val);
                               buckets[9].push_back(val);
                               buckets[12].push_back(val);
                               break;
                           }
                      case 'm':
                           {
                               buckets[5].push_back(val);
                               buckets[18].push_back(val);
                               break;
                           }
                      /*case 'e':
                           {
                               buckets[6].push_back(val);
                               break;
                           }*/
                      case ' ':
                           {
                               buckets[7].push_back(val);
                               buckets[10].push_back(val);
                               buckets[15].push_back(val);
                               break;
                           }
                      case 't':
                           {
                               buckets[8].push_back(val);
                               break;
                           }
                      /*case 'o':
                           {
                               buckets[9].push_back(val);
                               break;
                           }*/
                      /*case ' ':
                           {
                               buckets[10].push_back(val);
                               break;
                           }
                      case 'c':
                           {
                               buckets[11].push_back(val);
                               break;
                           }
                      case 'o':
                           {
                               buckets[12].push_back(val);
                               break;
                           }*/
                      case 'd':
                           {
                               buckets[13].push_back(val);
                               break;
                           }
                      /*case 'e':
                           {
                               buckets[14].push_back(val);
                               break;
                           }
                      /*case ' ':
                           {
                               buckets[15].push_back(val);
                               break;
                           }*/
                      case 'j':
                           {
                               buckets[16].push_back(val);
                               break;
                           }
                      case 'a':
                           {
                               buckets[17].push_back(val);
                               break;
                           }
                      /*case 'm':
                           {
                               buckets[18].push_back(val);
                               break;
                           }*/
     };
     //return;
}

void count_str_occ(int length,int iprev)
{
     char ch;
     int i=0;
     if(length==19)
     {
                   ::count++;
                   if(::count==10000)
                   ::count=0;
                   return;
     }
     //cout<<' '<<buckets[length].size();
     
     for(i=0;i<buckets[length].size();i++)
     {
                                          if(buckets[length][i]>iprev)
                                          count_str_occ(length+1,buckets[length][i]);
     }
     //cin>>ch;
     return;                                          
}

int main()
{
    char ch,curr_char,str[10];
    int i,j,k,n,N;
    
        
    FILE *fin=fopen("input.txt","r"),*fout=fopen("output.txt","w");
    fscanf(fin,"%d",&N);
    
    //printf("%d",N);
    //cin>>ch;
    curr_char=fgetc(fin);
    
    
    for(n=1;n<=N;n++)
    {
                     ::count=0;
                     curr_char=fgetc(fin);
                     //cout<<curr_char;
                     for(j=0;j<=19;j++)
                     buckets[j].erase(buckets[j].begin(),buckets[j].end());
                     for(i=0;(curr_char>=97 && curr_char<=122)||curr_char==32;i++)
                     {
                                            if(feof(fin))
                                            goto ads;
                                                                                                                        
                                                 
                                                 push_into_bucket(i,curr_char);
                                                 curr_char=fgetc(fin);
                                                 cout<<curr_char;
                     }
                     strcpy(str,"");
                     ::count_str_occ(0,-1);
                     if(::count/10==0)
                     strcpy(str,"000");
                     else if(::count/100==0)
                     strcpy(str,"00");
                     else if(::count/1000==0)
                     strcpy(str,"0");
                     fprintf(fout,"Case #%d: %s%d\n",n,str,::count);
                     //cin>>ch;
                     
    }
    ads:
    //cout<<::count;
    //cout<<n_test_cases;
    //cin>>ch;
    
    fclose(fin);
    fclose(fout);
    //fclose(fout);
    
    return 0;
}
