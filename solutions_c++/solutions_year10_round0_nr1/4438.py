#include <stdio.h>

bool isON(int noOfToggles, int noOfDevices){
	
	bool condition[40][2];	//1st - device gets power, 2nd - device on
	int powerCount = 1;
	
	for(int i = 1; i <= noOfDevices ; i++)
		condition[i][0] = condition[i][1] = false;
		
	//condition[0][0] = condition[0][1] = condition[1][0] = true;
	condition[1][0] = true;
	condition[noOfDevices+1][0] = condition[noOfDevices+1][1] = false;
	
	for(int i = 1 ; i <= noOfToggles ; i++){
			
			//for(int l = 1 ; l <= noOfDevices ; l++)
				//printf("#%d: %d %d\n",l,condition[l][0],condition[l][1]);
			//printf("toggle:%d\n",i);
			
			for(int j = 1 ; j <= noOfDevices ; j++){

					//if device had power then toggle switches (1)
					if(condition[j][0] == true){
						
						condition[j][1] ? condition[j][1] = false : condition[j][1] = true;

					}
					
			}
		
		for(int j = 2 ; j <= noOfDevices ; j++){
					
					if( condition[j-1][0] == false || condition[j-1][1] == false  )
						condition[j][0] = false;
					else condition[j][0] = true;
		}		
		
		if(powerCount < noOfDevices) powerCount++;
		
	}
	
	if( condition[noOfDevices][0] && condition[noOfDevices][1] )
		return true;
	return false;
}

int main(){
	
	int testCases, noOfDevices, noOfToggles;
	
	
	scanf("%d",&testCases);
	
	//device on and have to have power
	//snapping your fingers only has an effect if the Snapper is plugged 
	//in and is receiving power from the socket. 
	//light is plugged into the nth snapper
	
	for(int i = 1 ; i <= testCases ; i++){
		scanf("%d%d", &noOfDevices, &noOfToggles);
				
		printf("Case #%d: ",i);
		
		if( isON(noOfToggles,noOfDevices) )
			printf("ON\n");
		
		else printf("OFF\n");
	}
	
	return 0;	
}
