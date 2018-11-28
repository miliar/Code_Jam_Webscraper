#include<iostream>
#include<algorithm>
#include<list>
#include<fstream>
#include<vector>
#include<cstdlib>

using namespace std;

int main()
{
    	    

    	    ifstream fin;
	    fin.open("C-small-attempt0.in",ios::in);
	    
	    ofstream fout;
	    fout.open("C-small-attempt0.out",ios::out);

	    unsigned long int no_cases,people,run,no_groups;
	    vector<unsigned long int> v;
	    unsigned long int group,no_run,sum,sum2,k;
	    
	    fin>>no_cases;

	    
	    for( int i = 0; i < no_cases; i++)
	    {
	     	   fin>>run;
	    	   fin>>people;
	    	   fin>>no_groups;

		   v.clear();
		   for(int j = 0; j < no_groups; j++)
		   {
		    	     fin>>group;

			     v.push_back(group);
			     
		   }
		   no_run = 0;
		   sum = 0;
		   k = 0;
		   for(int j = 0; no_run<run; no_run++ )
		   {
		    	    sum2 = 0;
			    k = 0;
		    	    for(;sum2+v[j] <= people ;)
			    {
			     		  if(k>=v.size())
					  	    break;
					  sum2 += v[j];
//cout<<"\n sum2:"<<sum2<<" v[j]"<<v[j]<<" j"<<j;

			    		  j++;
					  k++;
					  j = j%v.size();
			    		  
			    
			    }

			    sum += sum2;

//cout<<"\nsum"<<sum;
//getchar();
			    

	
		   }
		   fout<<"Case #"<<i+1<<": "<<sum<<"\n";
		   v.clear();
	    }
//getchar();
	
}
