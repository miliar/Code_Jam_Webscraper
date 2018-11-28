//#include <stdlib>
#include <iostream>
#include <map>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    freopen("B.in" , "r" , stdin);
    freopen("B.out" , "w" , stdout);
    
    int T;   
    cin>>T;
    

    //{Q, W, E, R, A, S, D, F}. 
//    int 

     for(int caseID = 1 ; caseID <= T ; caseID ++){
		 map<string, char> combineSets;
		 map<char, char> delSets;
    map<char, int> invokeTimes;

             invokeTimes['Q'] = 0;  invokeTimes['W'] = 0;  invokeTimes['E'] = 0;  invokeTimes['R'] = 0;
              invokeTimes['A'] = 0;  invokeTimes['S'] = 0;  invokeTimes['D'] = 0;  invokeTimes['F'] = 0;
             
             int numCombine, numDel, numInvoke;
             char charCombine_1, charCombine_2, charCombine;
                        
             cin >> numCombine;
             
             for(int i=0; i<numCombine; i++){
                     cin>>charCombine_1;
                     cin>>charCombine_2;
                     cin>>charCombine;
                     
                     string str12, str21;
                     str12 += charCombine_1;str12 += charCombine_2;
                     str21 += charCombine_2;str21 += charCombine_1;
                     combineSets[str12] =charCombine; 
                     combineSets[str21] =charCombine;
                     
             }
             
             cin >> numDel;
             
             char charDel_1, charDel_2;
             
             for(int j=0; j<numDel; j++){
                     cin>>charDel_1;
                     cin>>charDel_2;

                     delSets[charDel_1] =charDel_2; 
                     delSets[charDel_2] =charDel_1;                     
             }
             
             char result[105]; char charInvokeCur=' ';char charInvokeLast=' ';
             int i_result=-1;
             cin>>numInvoke;
             for(int k=0; k<numInvoke; k++){
				 if(i_result == -1){
					 charInvokeLast=' ';
				 }else{
					 charInvokeLast = result[i_result];
				 }

                 string tryCombine;
                 cin>>charInvokeCur;
                 tryCombine += charInvokeLast; tryCombine += charInvokeCur;

                  if(combineSets.find(tryCombine) != combineSets.end()){
                           result[i_result] = combineSets[tryCombine];
                           invokeTimes[charInvokeLast] --;
                     }else if(delSets.find(charInvokeCur) != delSets.end()){
                                  
                           if(invokeTimes[(delSets.find(charInvokeCur)) ->second] != 0){
                                          i_result = -1;  
                                            invokeTimes['Q'] = 0;  invokeTimes['W'] = 0;  invokeTimes['E'] = 0;  invokeTimes['R'] = 0;
                                            invokeTimes['A'] = 0;  invokeTimes['S'] = 0;  invokeTimes['D'] = 0;  invokeTimes['F'] = 0;                                                
                           }else{
							   i_result++;
							   result[i_result] = charInvokeCur;
								invokeTimes[charInvokeCur] ++;

						   }
                     }else{
						 i_result++;
						 result[i_result] = charInvokeCur;
						 invokeTimes[charInvokeCur] ++;
					 }
                     
                     
                     //charInvokeLast = charInvokeCur;
             }
             
             //result[i_result] = "\0";
             
             cout<<"Case #"<<caseID<<": [";
             if(i_result != -1){
                  for(int i=0; i< i_result; i++){
                      cout<< result[i]<<", ";
                  } 
                  cout<< result[i_result];
             }
             cout<<"]\n";
             

     }
     

   // system("PAUSE");
    return 0;
}
