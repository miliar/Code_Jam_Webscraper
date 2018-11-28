#include<fstream>
#include<iostream>
using namespace std;

int main(){
    //se debe organizar de mayor a menor
    //a todos los mayores que se pueda se les aplica lo del best result, teniendo una tripleta sorprendente
    //se cuentan los resultados que se pueda
    fstream leer, escribir;
    
    leer.open("B-large.in", ios::in);
    escribir.open("googlers.out", ios::out);
    //escribir2.open("input.in", ios::out);
    
    int n, s, p, temp, i, j, T, k, base, mod, cont, ceros;
    leer>>T;
    //escribir2<<T<<endl;
    for(k=1;k<=T;k++){
        //cout<<k<<endl;
        cont=0;
        leer>>n>>s>>p;
        //escribir2<<k<<'\t'<<n<<' '<<s<<' '<<p<<' ';
        int nums[n];
        
        for(i=0;i<n;i++){
            leer>>nums[i];
            //escribir2<<nums[i]<<' ';
        }
        
        //escribir2<<endl;
        
        if(p==0){
            escribir<<"Case #"<<k<<": "<<n<<endl;
        }
        else if(s==n){
            i=0;
            bool evalue;
            while(i<n){
                mod = nums[i]%3;
                base = nums[i]/3;
                if(mod==0){
                    if(base+1>=p){
                        cont++;
                    }
                }
                if(mod==1){
                    if(base+1>=p){
                        cont++;
                    }
                }
                if(mod==2){
                    if(base+2>=p){
                        cont++;
                    }
                }
                i++;
            }
            escribir<<"Case #"<<k<<": "<<((cont<=n)?cont:n)<<endl;
        }
        else{
            for(i=0;i<n;i++)
                for(j=i+1;j<n;j++)
                    if(nums[j]>nums[i]){
                        temp = nums[j];
                        nums[j] = nums[i];
                        nums[i] = temp;
                    }
            
            ceros=0;
            for(i=0;i<n;i++)
                if(nums[i]==0)
                    ceros++;
            n-=ceros;
            
            i=0;
            j=0;
            bool evalue=true;
            while(evalue){
                mod = nums[i]%3;
                base = nums[i]/3;
                if(mod==0){
                    if(base>=p){
                        cont++;
                    }
                    else{
                        evalue=false;
                        i--;
                    }
                }
                if(mod==1){
                    if(base+1>=p){
                        cont++;
                    }
                    else{
                        evalue=false;
                        i--;
                    }
                }
                if(mod==2){
                    if(base+1>=p){
                        cont++;
                    }
                    else{
                        evalue=false;
                        i--;
                    }
                }
                i++;
            }
            
            while(j<s && i<n){
                mod = nums[i]%3;
                base = nums[i]/3;
                if(mod==0){
                    if(base+1>=p){
                        cont++;
                    }
                    j++;
                }
                if(mod==1){
                    if(base+1>=p){
                        cont++;
                    }
                }
                if(mod==2){
                    if(base+2>=p){
                        cont++;
                    }
                    j++;
                }
                i++;
            }
            while(i<n){
                mod = nums[i]%3;
                base = nums[i]/3;
                if(mod==0){
                    if(base>=p){
                        cont++;
                    }
                }
                if(mod==1){
                    if(base+1>=p){
                        cont++;
                    }
                }
                if(mod==2){
                    if(base+1>=p){
                        cont++;
                    }
                }
                i++;
            }
            
            escribir<<"Case #"<<k<<": "<<((cont<=n)?cont:n)<<endl;
        }
    }
    
    leer.close();
    escribir.close();
    
    return 0;
}
