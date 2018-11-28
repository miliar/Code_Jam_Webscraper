#include<stdio.h>
#include<iostream>
#include<fstream>


using namespace std;

int L,D,N,count;

char string_vector[5005][20],choices_str[20][400],temp_str[20];

/*bool check_occ()
{
     int i;
     for(i=0;i<=D-1;i++)
     {
                        if(temp_str.compare(string_vector[i])==0)
                        return true;
     }
     return false;
}

void find_n_occ(int depth)
{
     cout<<temp_str<<endl;
    if(depth==L)
    {
                if(check_occ())
                {::count++;cout<<temp_str;
                ;}
                return;
    }
    
    int i;
    for(i=0;i<=choices_str[depth].length();i++)
    {
                                               temp_str.erase(depth,L-depth);
                                               temp_str.push_back(choices_str[depth][i]);
                                               find_n_occ(depth+1);
    }
    return;
}
*/
void find_n_occo()
{
     int d,l,i;
     for(d=0;d<=D-1;d++)
     {
                        for(l=0;l<=L-1;l++)
                        {
                                           for(i=0;i<=strlen(choices_str[l])-1;i++)
                                           if(string_vector[d][l]==choices_str[l][i])
                                           break;
                                           if(i==strlen(choices_str[l]))
                                           goto ads;
                        }
                        ::count++;
                        ads:l=0;
     }
                        
}


int main()
{
    char ch,word[450],str[20]="";
    int i,j,k,n;
    
        
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin>>L>>D>>N;
    cout<<N;
    for(i=0;i<=D-1;i++)
    fin>>string_vector[i];
    
    
    for(n=1;n<=N;n++)
    {
                     cout<<n<<endl;
                     //cin>>ch;
                     for(j=0;j<=200;j++)
                     word[j]='\0';
                     fin>>word;
                     //cout<<' '<<word<<endl;
                     ::count=0;
                     i=0;
                     cout<<'a';
                     for(k=0;k<=L-1;k++)
                     {
                                        for(j=0;j<=200;j++)
                                        choices_str[k][j]='\0';
                                        //cout<<" str:"<<choices_str[k];
                                        if(word[i]!='(')
                                        choices_str[k][0]=word[i];
                                        else 
                                        {
                                        j=0;
                                        while(true)
                                        {
                                                           i++;
                                                           if(word[i]==')')
                                                           break;
                                                           choices_str[k][j]=word[i];
                                                           j++;
                                                           cout<<'a';
                                                           
                                        }
                                        }
                                        //cin>>ch;
                                        i++;
                                        //cout<<" str :"<<choices_str[k];
                     }
                     
                     
                     //cout<<choices_str[1]<<endl<<string_vector[24];
                     find_n_occo();
                     //cin>>ch;
                     //cout<<"Case #"<<n<<": "<<::count<<' '<<n<<endl;
                     //cin>>ch;
                     fout<<"Case #"<<n<<": "<<::count<<endl;
                     //cin>>ch;
    }
    
    //cout<<n_test_cases;
    //cin>>ch;
    
    fout.close();
    fin.close();
    
    
}
