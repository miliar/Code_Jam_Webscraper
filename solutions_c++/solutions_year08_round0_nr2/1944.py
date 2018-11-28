#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<utility>
using namespace std;

typedef pair<int,int> pint;

bool mycomp (pint i,pint j) { return (i.first < j.first); }

int main()
{
	int cases;
	vector<pint> a,b;
    vector<int> cova,covb;
	int na,nb,n,t,i,j,k,l;
	
	int hr,min,t1,cnta,cntb,caseno=1,prevside,mini,miniidx;
	pint prev;
	
	cin>>cases;

	while(cases--)
	{

		cin>>t>>na>>nb;
		
		a.clear();
        b.clear();
        cova.clear();
        covb.clear();
        
		for(i=0;i<na;i++)
		{
            scanf("%d:%d",&hr,&min);
            t1= hr*60+min;
            scanf("%d:%d",&hr,&min);
            a.push_back(pair<int,int>(t1,hr*60+min));
            cova.push_back(0);
		}

		for(i=0;i<nb;i++)
		{
            scanf("%d:%d",&hr,&min);
            t1= hr*60+min;
            scanf("%d:%d",&hr,&min);
            b.push_back(pair<int,int>(t1,hr*60+min));
            covb.push_back(0);
		}
     
        sort(a.begin(),a.end(),mycomp);
        sort(b.begin(),b.end(),mycomp);
        
/*        
        for(i=0;i<na;i++)
        {                cout<<a[i].first<<" "<<a[i].second<<endl;
        }
        cout<<endl;
        
        for(i=0;i<nb;i++)
        {                cout<<b[i].first<<" "<<b[i].second<<endl;
        }
        cout<<endl;
*/        
        
        i=j=0;
        cnta=cntb=0;

        
        
        while(1)
        {
         while(i<na && cova[i]) i++;
         while(j<nb && covb[j]) j++;
         
         if(i==na)
         {
             for(k=0;k<nb;k++)
             {
                              if(!covb[k]) cntb++;
             }
              break;     
         }
         else if(j==nb)
         {
             for(k=0;k<na;k++)
             {
                              if(!cova[k]) cnta++;
             }
              break;     
                       
         }
                 
         if(a[i].first<=b[j].first)
         {
            cova[i]=1;
           // cout<<"seta"<<i<<endl;
            prevside=1;
            prev=a[i];
            cnta++;
         }
          else
          {
            covb[j]=1;
          //  cout<<"setb"<<j<<endl;
            prevside=2;
            prev=b[j];
            cntb++;
         }


         while(1)
         {
             mini=24*60;
             miniidx=-1;
    
             if(prevside==2)
             {
                 for(k=0;k<na;k++)
                 {
                            if(cova[k]) continue;
                            if(a[k].first>=prev.second + t)
                            {
                                   if(a[k].second<mini)
                                   {
                                                       mini=a[k].second;
                                                       miniidx=k;
                                   }
                            }
                                                        
                }
                if(miniidx!=-1)
                {
                              cova[miniidx]=1;
                              prevside=1;
                              prev=a[miniidx];
           //                   cout<<"a"<<miniidx<<endl; 
                }
                else
                    break;
            
            }
            else
            {
                 for(k=0;k<nb;k++)
                 {
                            if(covb[k]) continue;
                            if(b[k].first>=prev.second + t)
                            {
                                   if(b[k].second<mini)
                                   {
                                                       mini=b[k].second;
                                                       miniidx=k;
                                   }
                            }
                                                        
                }
                if(miniidx!=-1)
                {
                              covb[miniidx]=1;
                              prevside=2;
                              prev=b[miniidx]; 
            //                  cout<<"b"<<miniidx<<endl;
                }
                else
                    break;
            }
        
        } //while(1)
        
        
        } //outer while(1) 
        
             
		cout<<"Case #"<<caseno++<<": "<<cnta<<" "<<cntb<<endl;
	}
	return 0;
}	
