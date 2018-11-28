 #include <iostream>
 #include <vector>
 using namespace std;
 
 
 int main (){
	int t;
	cin>>t;
	for (int i=0;i<t;i++){
		int n;
		cin>>n;
		char secr[n];
		int secn[n];
		vector <int> nb,no;
		for (int j=0;j<n;j++){
			cin>>secr[j];
			cin>>secn[j];
			if (secr[j]=='B'){
				nb.push_back(secn[j]);
			}else if (secr[j]=='O'){
				no.push_back(secn[j]);
			}
		}
		int cont=0,ind=0,indo=0,indb=0;
		int poa=1,pba=1;
		for (;;){
			char roba;
			roba=secr[ind];
			//cout<<"llegue"<<endl;
			if (roba=='B'){
				if (no.empty()==false){
					if (poa<no[indo]){ //otro robot no principal
						poa++;
					}else if (poa>no[indo]){
						poa--;
					}
				}
				
				if (pba==nb[indb]){ //accion del rob principal
					ind++;
					indb++;
				}else if(pba>nb[indb]){
					pba--;
				}else if(pba<nb[indb]){
					pba++;
				}
				cont++;
			}else if (roba=='O'){
				if (nb.empty()==false){
					if (pba<nb[indb]){	//otro rob no principal
						pba++;
					}else if (pba>nb[indb]){
						pba--;
					}
				}
				
				if (poa==no[indo]){		 //acciones del rob principal
					ind++;
					indo++;
				}else if(poa>no[indo]){
					poa--;
				}else if(poa<no[indo]){
					poa++;
				}
				cont++;
			}
			if (ind==n){
				cout<<"Case #"<<i+1<<": "<<cont<<endl;
				cont=0,ind=0,indo=0,indb=0;
				poa=1,pba=1;
				break;
			}
		}
	}
	return 0; 
 }
	 
	 
