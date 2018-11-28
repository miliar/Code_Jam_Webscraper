// NextNumber.cpp: define el punto de entrada de la aplicación de consola.
//

#include "stdafx.h"
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

vector <int> p;

void swap(int i, int j) {
 
		int t= p[i];
		p[i]= p[j];
		p[j]= t;
	}


bool nextPerm() {
 
		int n= p.size();
		int i= n;

        i--;
		if (i < 1) 
			return false;
        
		for(;;) {
			int ii= i--;
			if (p[i] < p[ii]) {
				int j= n;
				while (!(p[i] < p[--j]));
				swap(i, j);
				for (j= n; j > ii; swap( --j, ii++));
				return true;
			}
			if (i == 0) {
				for (int j= n; j > i; swap( --j, i++));
				return false;
			}
		}
	}




int _tmain(int argc, _TCHAR* argv[])
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);



    int zz;
    scanf("%d\n", &zz);
    for(int z=0;z<zz;z++)
    {
        int n;
        
        char buffer[100];
        int siz=0;
        vector<int> num;        
        scanf("%c",&buffer[siz]);        
        while(buffer[siz]!='\n'){
            num.push_back(buffer[siz]-'0');            
            siz++;
            scanf("%c",&buffer[siz]);        
        }
        

        int i=0;

        vector<int> list;


        //num.push_back(0);
        //num.push_back(0);
        //num.push_back(0);
        //num.push_back(0);

        //sort(num.begin(),num.end());
        p=num;
        if(nextPerm()==false){
            /*
            bool eq=true;
            for(i=0;i<p.size();i++)
                if(p[i]!=num[i])
                {
                    eq=false;
                    break;
                   
                }

                    
           if(eq)
           {
                printf("Case #%d: ", z+1);
            for(i=0;i<num.size();i++)
                printf("%d",num[i]);
            printf("*\n");
                continue;

           }
            
           else{*/
               vector<int> nnum;
               nnum.push_back(0);
               for(int j=0;j<num.size();j++)
                   nnum.push_back(num[j]);
               p=nnum;
               nextPerm();
      
           //}

        }
//        do
 //       {   
//            int tmp=0;
//            for(i=0;i<num.size();i++)
//                tmp+=num[i]*(int)pow(10.0,(int)(num.size()-i-1));

          //  list.push_back(tmp);


   //     }while(next_permutation(num.begin(),num.end()));
        
        

        /*sort(list.begin(),list.end());

        for(i=0;i<list.size();i++){
            if(list[i]>n)
                break;
        }
        */
            /*
        if(tmp<=n)
        {

            num.push_back(0);
            sort(num.begin(),num.end());
            do
           {   
            int tmp=0;
            for(i=0;i<num.size();i++)
                tmp+=num[i]*(int)pow(10.0,(int)(num.size()-i-1));

            list.push_back(tmp);


            }while(next_permutation(num.begin(),num.end()));    

           for(i=0;i<list.size();i++){
               if(list[i]>n)
                   break;
           }

            printf("Case #%d: %d\n", z+1,list[i]);
            continue;


        }
        */


//        else if(tmp<10)
//            tmp=n*10;
        
        

        printf("Case #%d: ", z+1);
        for(i=0;i<p.size();i++)
            printf("%d",p[i]);
        printf("\n");
        


    }

	return 0;
}

