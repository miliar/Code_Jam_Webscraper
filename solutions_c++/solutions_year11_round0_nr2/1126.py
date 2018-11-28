#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <map>

using namespace std;

int main()
{
    int t,n,c,d,i,j,k,l;
    string spells,temp,combo1,combo2;
   
    map<string,char> res,resx;
    map<string,char>::iterator it;
        
    fstream fin,fout;
    fin.open("a.in",ios::in);
    fout.open("a.out",ios::out);
    
    fin >> t;
    for(i=0;i<t;i++)
    {
        res.clear();
        resx.clear();
        
        fin >> c;
        for(j=0;j<c;j++)
        {
            fin>>temp;
            combo1=temp;
            combo1[2]='\0';
            combo2=combo1;
            combo2[1]=combo1[0];
            combo2[0]=combo1[1];
            
            res[combo1]=res[combo2]=temp[2];
            //cout<<temp<<endl;
        }
        fin >> d;
        for(j=0;j<d;j++)
        {
            fin>>temp;
            combo1=temp;
            combo1[2]='\0';
            combo2=combo1;
            combo2[1]=combo1[0];
            combo2[0]=combo1[1];
            resx[combo1]=resx[combo2]='-';
            //cout<<temp<<endl;
        }   
        fin >> n;  
        fin >> spells;   
        //end input
        
        //for ( it=resx.begin() ; it != resx.end(); it++ )
        //    cout <<'.'<< (*it).first <<'.'<< " => " << (*it).second << endl;
        //cout<<"Old: "<<spells<<endl;
        for(j=1;j<n;j++)
        {
            combo1="###";
            combo1[0]=spells[j-1];
            combo1[1]=spells[j];  
            combo1[2]='\0';   
            //cout<<combo1<<endl;  
   
            if(res.find(combo1)!=res.end())
            {
                spells[j-1]=res[combo1];
                for(k=j;k<n-1;k++)
                {
                    spells[k]=spells[k+1];
                }
//                spells[k]='\0';
               
                spells.erase(k);
                n=spells.length();
                //cout<<"+New: "<<spells<<endl;
                j--;
            }
            else
            {
                for(k=0;k<j;k++)
                {
                    combo2="##";
                    combo2[0]=spells[j];
                    combo2[1]=spells[k];  
                    combo2[2]='\0';   
                    if(resx.find(combo2)!=resx.end())
                    {
                        //cout<<"Del";
                        for(l=j+1;l<n;l++)
                        {
                            spells[l-j-1]=spells[l];
                        }
                        spells[l-j-1]='\0';
                        spells.erase(l-j-1);
                        n=spells.length();
                        //cout<<"-New: "<<spells.c_str()<<endl;
                        
                        j=-1;
                    }
                }
            }
                
        }
        //cout<<spells.length()<<endl;   
        fout<<"Case #"<<i+1<<": [";
        for(j=0;j<n;j++)
        {
            fout<<spells[j];
            if(j!=n-1)
                fout<<", ";
        }
        
        fout<<"]"<<endl;
        //cout<<n<<endl;
        }
  
    return 0;
}
