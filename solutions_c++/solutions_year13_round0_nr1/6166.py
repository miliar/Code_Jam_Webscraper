#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
    ofstream fo("output.txt");
    ifstream fi("data.txt");
    
	string lines;
    getline(fi,lines);
    int cases=0;
    if(lines.size()>1)
		for(int i=0;i<lines.size();++i)
			cases=cases * 10 + (lines[i]-'0');
    else
        cases = lines[0]-'0';  
    int i=0;

	for(;i<cases;++i)
	{
begin:
		   if(i== cases)
		   {
			   fi.close();
			   fo.close();
			   return 0;
		   }
//		   cout << i << endl;
		   char ans[4][4]={'.'};
           int dotCount=0;
           for(int j=0;j<4;++j)
		   {				
			   string str = "";
			   getline(fi,str,'\n');
			   if(str.size() >0)
			   {
				   for(int k=0;k<4;++k)
				 {	
					ans[j][k] = str[k];
//					cout << ans[j][k];
				 }
			   }
			   else
			   {
				   getline(fi,str,'\n');
				   for(int k=0;k<4;++k)
				 {	
					ans[j][k] = str[k];
//					cout << ans[j][k];
				 }
			   }
			   cout << endl;
		   }
		   int xCount=0;
           int xCount2=0;
           int xCount3=0;
           int oCount=0;
           int oCount2=0;
           int oCount3=0;
           int tCount=0; 
           int tCount2=0;
           int tCount3=0;
           for(int j=0;j<4;++j)
         { 
			 xCount=0;
			 oCount=0;
			 tCount=0;
			for(int k=0;k<4;++k)
			{
				switch(ans[j][k])
				{
                  case('X'):
                  {    ans[j][k] = 'X';
                       xCount++;
                       if(j==k)
                           xCount2 ++;
                       if(j+k == 3)
							xCount3 ++;	
                       break;
					}
				case('O'):
                  {    ans[j][k] = 'O';
                       oCount++;
						if(j==k)
                           oCount2 ++;
                       if(j+k == 3)
							oCount3 ++;	
                       break;
		          }
				case('T'):
                  {
 					   ans[j][k] = 'T';
					   tCount++;
					   if(j==k)
                           tCount2 ++;
					   if(j+k == 3)
						   tCount3 ++;	
						break;				
				  }	
				case('.'):
                  {
 						dotCount++;
						break;				
				  }	
			} // switch
	    } // k
            if(((xCount == 3) && (tCount == 1)) ||(xCount == 4))
            {
				fo << "Case #" << i+1 << ":" << " X won" << endl;
				++i;
                goto begin;
	        }	
            if(((oCount == 3) && (tCount == 1)) ||(oCount == 4))
            {  
			   fo << "Case #" << i+1 << ":" << " O won" << endl;
			   ++i;
			   goto begin;            
			}
	    
            if(((xCount2 == 3) && (tCount2 == 1)) ||(xCount2 == 4))
            {
			   fo << "Case #" << i+1 << ":" << " X won" << endl;
               ++i;
			   goto begin; 
			}	
            if(((oCount2 == 3) && (tCount2 == 1)) ||(oCount2 == 4))
            {  
			   fo << "Case #" << i+1 << ":" << " O won" << endl;
			   ++i;
			   goto begin; 	             
			}	
	
            if(((xCount3 == 3) && (tCount3 == 1)) ||(xCount3 == 4))
            {
			   fo << "Case #" << i+1 << ":" << " X won" << endl;
               ++i;
			   goto begin; 
			}	
            if(((oCount3 == 3) && (tCount3 == 1)) ||(oCount3 == 4))
            {  
				fo << "Case #" << i+1 << ":" << " O won" << endl;
				++i;
				goto begin;             
			}	
	  } // j
     	    for(int j=0;j<4;++j)
          {
            int xCount=0;
            int oCount=0;
            int tCount=0;
            for(int k=0;k<4;++k)
            {
              switch(ans[k][j])
              {
					case('X'):
                  {   
                       xCount++;
                       break;
				  }
				   case('O'):
                  {   
                       oCount++;
						break;
					}
				  case('T'):
                  {
                       tCount++;
                       break;	    				
				 }	
			  }// switch 
	    }//k
	        if(((xCount == 3) && (tCount == 1)) ||(xCount == 4))
            {
				fo << "Case #" << i+1 << ":" << " X won" << endl;
                ++i;
				goto begin; 
			}	
            if(((oCount == 3) && (tCount == 1)) ||(oCount == 4))
            {  
			    fo << "Case #" << i+1 << ":" << " O won" << endl;
		        ++i;
				goto begin;           
			}	
	  }//j	 
      	  if(dotCount >0)
			  fo << "Case #" << i+1 << ":" << " Game has not completed" << endl;
          else                 	
			  fo << "Case #" << i+1 << ":" << " Draw" << endl;
	} // cases

  fi.close();
  fo.close();
  return 0;
}