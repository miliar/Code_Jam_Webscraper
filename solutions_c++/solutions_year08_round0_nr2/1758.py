#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

class Hora{
	public:
	int hour;
	int min;
	
	Hora(int aa, int b){
		hour=aa;
		min=b;
	}
	
	Hora(){
		hour=0;
		min=0;
	}
	
	bool operator<(Hora b){
		if (hour!=b.hour)
			return hour<b.hour;
		return min<b.min;
	}
	
	bool operator>(Hora b){
		if (hour!=b.hour)
			return hour>b.hour;
		return min>b.min;
	}
	
	
	bool operator<=(Hora b){
		if (hour!=b.hour)
			return hour<=b.hour;
		return min<=b.min;
	}
	
	Hora operator+(int num){
		Hora re = Hora(hour,min);
		//cout << "Sumando " << re.hour << ":" << re.min << " con " << num << endl;
		re.min+=num;
		//cout << re.min << " Minutos\n";
		re.hour+=re.min/60;
		re.min%=60;
		//cout << re.hour << ":" << re.min << endl;
		return re;
	}
	
	void operator=(Hora b){
		hour=b.hour;
		min=b.min;
	}
	
};

class ruta{
	public:
	Hora salida;
	Hora llegada;
	bool a;
	
	ruta(Hora uno , Hora dos, bool per){
		salida=uno;
		llegada=dos;
		a=per;
	}
	
	ruta(){
		salida=Hora();
		llegada=Hora();
		a=false;
	}
	
	ruta operator<(ruta b){
		llegada<b.llegada;
	}
	
	ruta operator<=(ruta b){
		llegada<=b.llegada;
	}
	
	ruta operator>(ruta b){
		llegada>b.llegada;
	}
		
};

int main(){
	int casos;
	cin >> casos;
	for (int caso=0 ; caso<casos ;caso++){
		int rotacion;
		cin >> rotacion;
		int desdeA, desdeB;
		cin >> desdeA >> desdeB;
		vector<ruta> rutaA;
		vector<ruta> rutaB;
		//vector<ruta> rutaT;
		bool tachadosA[desdeA];
		bool tachadosB[desdeB];
		memset(tachadosA  , false , sizeof(tachadosA));
		memset(tachadosB  , false , sizeof(tachadosB));
		for (int i=0 ; i<desdeA ; i++){
			int a,b,c,d;
			scanf("%d" , &a);
			getchar();
			scanf("%d %d" , &b , &c);
			getchar();
			scanf("%d" , &d);
			rutaA.push_back(ruta(Hora(a,b),Hora(c,d),true));
			//cout << a << ":" << b << " " << c << ":" << d << endl;
		}
		for (int i=0 ; i<desdeB ; i++){
			int a,b,c,d;
			scanf("%d" , &a);
			getchar();
			scanf("%d %d" , &b , &c);
			getchar();
			scanf("%d" , &d);
			rutaB.push_back(ruta(Hora(a,b),Hora(c,d),true));
			//cout << a << ":" << b << " " << c << ":" << d << endl;
		}
		//sort(rutaA.begin() , rutaA.end());
		//sort(rutaB.begin() , rutaB.end());
		int tachadosTotalB=0;
		int tachadosTotalA=0;
		for (int i=0 ; i<desdeA ; i++){
			//bool salir=false;
			Hora menor=Hora(99,99);
			int menorid=-1;
			for (int j=0 ; j<desdeB ; j++){
			//	cout << j << endl;
				Hora temp = rutaA[i].llegada+rotacion;
				//cout << temp.hour << ":" << temp.min << endl;
				if (rutaA[i].llegada+rotacion<=rutaB[j].salida && !tachadosB[j]){
					//salir=true;
					//tachadosB[j]=true;
					if (menorid!=-1){
						if (rutaB[j].salida<menor){
							menorid=j;
							menor=rutaB[j].salida;
						}
					}else{
						menorid=j;
						menor=rutaB[j].salida;
					}
			//		cout << "Tacho " << j << " con " << i << endl;
				//	cout << rutaA[i].llegada.hour << ":" << rutaA[i].llegada.min << " con " << cout << rutaB[j].salida.hour << ":" << rutaB[j].salida.min;
				//	
				}else{
					//cout << "No es menor que " << rutaB[j].salida.hour << ":" << rutaB[j].salida.min << "\n";
				}
			}
			if (menorid!=-1){
				//cout << "TAcho a " << menorid << endl;
				tachadosB[menorid]=true;
				++tachadosTotalB;
			}
		}
		//cout << "---------" << endl;
		for (int i=0 ; i<desdeB ; i++){
			//bool salir=false;
			Hora menor=Hora(99,99);
			int menorid=-1;
			for (int j=0 ; j<desdeA ; j++){
			//	cout << j << endl;
			
				Hora temp = rutaB[i].llegada+rotacion;
			//	cout << temp.hour << ":" << temp.min << endl;
				if (rutaB[i].llegada+rotacion<=rutaA[j].salida && !tachadosA[j]){
				//	salir=true;
					//tachadosA[j]=true;
					
					if (menorid!=-1){
						if (rutaA[j].salida<menor){
							menorid=j;
							menor=rutaA[j].salida;
						}
					}else{
						menorid=j;
						menor=rutaA[j].salida;
					}
					
					
					//cout << "Tacho " << j << " con " << i << endl;
				//	cout << rutaB[i].llegada.hour << ":" << rutaB[i].llegada.min << " con " << cout << rutaA[i].salida.hour << ":" << rutaA[i].salida.min;
					
				}else{
					//cout << "No es menor que " << rutaA[j].salida.hour << ":" << rutaA[j].salida.min << "\n";
				}
				
					
				
			}
			
			if (menorid!=-1){
			//	cout << "TAcho a " << menorid << endl;
				tachadosA[menorid]=true;
				++tachadosTotalA;
			}
			
		}
		cout << "Case #" <<  (caso+1) << ": " << desdeA-tachadosTotalA << " " <<desdeB-tachadosTotalB << endl;
	}
	return 0;
}
