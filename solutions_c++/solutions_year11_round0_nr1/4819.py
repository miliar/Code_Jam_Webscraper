#include<iostream>
#include<cmath>
using namespace std;
int main(){
    int t;
    cin >> t;
    for(int i = 0; i < t;i ++){
            
            int j;
            cin >> j;
            
            char znak;
            int dlugosc;
            int start1 = 1, start2 = 1;
            int result = 0;
            char poprzedniZnak = ' ';
            int suma = 0;
            while(j!=0){
                        j--;
                        cin >> znak >> dlugosc;
                        
                        
                        if(poprzedniZnak == ' ' || poprzedniZnak == znak){
                                         int temp = start1 - dlugosc;
                                         if(temp < 0) temp *= -1;
                                         temp++;
                                         
                                         suma += temp;
                                         result += temp;
                                         
                                         start1 = dlugosc;
                                         }
                                         
                                         
                        else {
                             
                             int temp = start2 - dlugosc;
                             if(temp < 0) temp *= -1;
                             temp++;
                             
                             result += temp;
                             temp = dlugosc;
                             while((dlugosc - 1) > 0 && suma > 0){
                                        result--;
                                        suma--;
                                        }
                             suma = 0;
                             
                             temp = start1;
                             start1 = start2;
                             start2 = temp;
                             
                             start1 = dlugosc;
                             
                             
                             
                             
                             }
                             
                        poprzedniZnak = znak;
                        

                        
                        
                        
                        
                        }
            
            cout << "Case #" << i + 1 << ": " << result << endl;
            
            
            
            
            }
    
    
return 0;    
}
