#include<iostream>
#include<fstream>
#include<cstdlib>

using namespace std;


void solve(int case_number,ostream* output,int* orange,int* orange_priority,int orange_length,int* blue,int* blue_priority,int blue_length)
{
	int time = 0;
	int i = 0;
	int j = 0;

	while(true){
		
		if(i>=orange_length && j>=blue_length){
			break;
		}else if(i>=orange_length){
			time += (blue[j]+1);
			j++;
		}else if(j>=blue_length){
			time += (orange[i]+1);
			i++;
		}else if(orange[i]==0){
			if(orange_priority[i]>blue_priority[j]){
				if(blue[j])blue[j]--;
				time++;
				i++;
			}else{
				time += (blue[j]+1);
				j++;
			}
		}else if(blue[j]==0){
			if(blue_priority[j]>orange_priority[i]){
				if(orange[i])orange[i]--;
				time++;
				j++;
			}else{
				time += (orange[i]+1);
				i++;
			}			
		}else if(orange[i]==blue[j]){
			time += orange[i];
			orange[i] = 0;
			blue[j] = 0;
		}else if(orange[i]>blue[j]){
			time += blue[j];
			orange[i] -= blue[j];
			blue[j]=0;
		}else if(blue[j]>orange[i]){
			time += orange[i];
			blue[j] -= orange[i];
			orange[i]=0;
		}
	}
	*output << "Case #" << case_number << ": " << time << std::endl;
}

int main()
{
	int number_cases;
	int number_entries;
	ifstream input("A-large.IN");
	ofstream output("output.txt");
	char color;
	int temp;
	int orange_length;
	int blue_length;
	int last_position_orange;
	int last_position_blue;
	
	input >> number_cases;

	for(int i=0;i<number_cases;i++){
	
		input >> number_entries;

		int orange[number_entries];
		int orange_priority[number_entries];
		int blue[number_entries];
		int blue_priority[number_entries];
		orange_length = blue_length =0;
		
		while(number_entries){
			input >> color;
			input >> temp;

			if(color=='O'){
				if(orange_length==0){
					orange[orange_length] = abs(temp - 1);
				}else{
					orange[orange_length] = abs(temp - last_position_orange);					
				}					
				orange_priority[orange_length] = number_entries;				
				orange_length++;
				last_position_orange = temp;
			}else if(color=='B'){
				if(blue_length==0){
					blue[blue_length] = abs(temp - 1);				
				}else{
					blue[blue_length] = abs(temp - last_position_blue);					
				}	
				blue_priority[blue_length] = number_entries;					
				blue_length++;
				last_position_blue = temp;
			}
			number_entries--;
		}
		solve(i+1,&output,&orange[0],&orange_priority[0],orange_length,&blue[0],&blue_priority[0],blue_length);
	}
	
	return 0;
}
