#include<iostream>
#include<conio.h>
#include<string>
#include<xstring>
#include<fstream>
#include<sstream>
#include<vector>
using namespace std;
void main()
{
	int n=0,c,i,d=0,g=0,s=0;
	
	string string1,item1[5],listLength;
	ifstream input("A.in");
	ofstream output("A.out");
	if(output == NULL)
	{
		cout<<"can not opent file"<<endl;
	}


	input >> n;
		
	getline(input,string1);
	string elemList[10000] = {""};
	for (int j = 0; j < n; j++)
	{
		cout<<endl;
		
		int elemCount = NULL;
		int elemCount1 = 0,elemCount2 = 0;
		cout << "case #"<<j+1<<": ";
		output << "Case #"<<j+1<<": ";
		
		getline(input,string1);
		//cout<<string1;
		std::istringstream wordstream(string1);
		std::string word;
		int x=0;
		while(wordstream >> word)
		{
			item1[x] = word;
			x++;
		}
		int len = item1[0].size();
		int len1 = item1[1].size();
		int up = atoi(item1[0].c_str());
		int down = atoi(item1[1].c_str());
		
		if (len == 1 && len1 == 1)
		{
			
		}
		
		else{
			s=0;
			elemCount = 0;
			for (g = up; g <= down; g++){
				int temp2 = g;
				int tempCount=0,tempCount1=0;
				string temp, temp3;
				stringstream convert; 
				convert << temp2;
				temp = convert.str();
				temp3 = temp;
				int elements;
				
	/*			for (c =0; c < len; c++){
					if ( temp3[0] == temp3[c]){
						tempCount = tempCount+1;
					}
				}	*/			
				if (tempCount == len )
				{
				}
				else{

						for (d = 0; d <= len-1; d++){	
							if ( d == 0){
								temp3[d] = temp[len-1];
							}
							else{
								temp3[d] = temp[d-1];
							}
						}
						int val = atoi(temp3.c_str());
							if( val >= up && val <= down)
							{
								if ( temp3 > temp)
								{
								
				//				output << temp<<"--> ";
				//				output << temp3<<" ";
								elemList[s] = temp3;
								s = s+1;
								elemCount++;
								}
							}
					
				
	
						if ( len >= 3 )
						{
							for (d = 0; d <= len-1; d++){	
							
								if ( d == 0){
									temp3[d] = temp[len-2];
						
								}
								else if ( d == 1){
									temp3[d] = temp[len-1];
								}
						
								else{
									temp3[d] = temp[d-2];
								}
							}
							int val = atoi(temp3.c_str());
							if( val >= up && val <= down)
							{
								if ( temp3 > temp)
								{
								
				//				output << temp<<"--> ";
				//				output << temp3<<" ";
								elemList[s] = temp3;
								s = s+1;
								elemCount++;
								}
							}
						}	
	
	
						if ( len >= 4 )
						{
							for (d = 0; d <= len-1; d++){	
							
								if ( d == 0){
									temp3[d] = temp[len-3];
						
								}
								else if ( d == 1){
									temp3[d] = temp[len-2];
								}
								else if ( d == 2){
									temp3[d] = temp[len-1];
								}
								
								else{
									temp3[d] = temp[d-3];
								}
							}
							int val = atoi(temp3.c_str());
							if( val >= up && val <= down)
							{
								if ( temp3 > temp)
								{
								
				//				output << temp<<"--> ";
				//				output << temp3<<" ";
								elemList[s] = temp3;
								s = s+1;
								elemCount++;
								}
							}
						}	
	

						if ( len >= 5 )
						{
							for (d = 0; d <= len-1; d++){	
							
								if ( d == 0){
									temp3[d] = temp[len-4];
						
								}
								else if ( d == 1){
									temp3[d] = temp[len-3];
								}
								else if ( d == 2){
									temp3[d] = temp[len-2];
								}
								else if ( d == 3){
									temp3[d] = temp[len-1];
								}
								else{
									temp3[d] = temp[d-4];
								}
							}
							int val = atoi(temp3.c_str());
							if( val >= up && val <= down)
							{
								if ( temp3 > temp)
								{
								
				//				output << temp<<"--> ";
				//				output << temp3<<" ";
								elemList[s] = temp3;
								s = s+1;
								elemCount++;
								}
							}
						}	
	
							if ( len >=6 )
						{
							for (d = 0; d <= len-1; d++){	
							
								if ( d == 0){
									temp3[d] = temp[len-5];
						
								}
								else if ( d == 1){
									temp3[d] = temp[len-4];
								}
								else if ( d == 2){
									temp3[d] = temp[len-3];
								}
								else if ( d == 3){
									temp3[d] = temp[len-2];
								}
								else if ( d == 4){
									temp3[d] = temp[len-1];
								}
								else{
									temp3[d] = temp[d-5];
								}
							}
							int val = atoi(temp3.c_str());
							if( val >= up && val <= down)
							{
								elemCount++;
			//					output << temp<<"--> ";
			//					output << temp3<<" ";
								elemList[s] = temp3;
								s = s+1;
						
							}
						}	
	
							if ( len >=7 )
						{
							for (d = 0; d <= len-1; d++){	
							
								if ( d == 0){
									temp3[d] = temp[len-6];
						
								}
								else if ( d == 1){
									temp3[d] = temp[len-5];
								}
								else if ( d == 2){
									temp3[d] = temp[len-4];
								}
								else if ( d == 3){
									temp3[d] = temp[len-3];
								}
								else if ( d == 4){
								temp3[d] = temp[len-2];
								}
								else if ( d == 5){
									temp3[d] = temp[len-1];
								}
								else{
									temp3[d] = temp[d-6];
								}
							}
							int val = atoi(temp3.c_str());
							if( val >= up && val <= down)
							{
								elemCount = elemCount + 1;
			//					output << temp<<"--> ";
			//					output << temp3<<" ";
								elemList[s] = temp3;
								s = s+1;
						
							}
						}	
	
							if ( len >=8 )
						{
							for (d = 0; d <= len-1; d++){	
							
								if ( d == 0){
									temp3[d] = temp[len-7];
						
								}
								else if ( d == 1){
									temp3[d] = temp[len-6];
								}
								else if ( d == 2){
									temp3[d] = temp[len-5];
								}
								else if ( d == 3){
									temp3[d] = temp[len-4];
								}
								else if ( d == 4){
									temp3[d] = temp[len-3];
								}
								else if ( d == 5){
									temp3[d] = temp[len-2];
								}
								else if ( d == 6){
									temp3[d] = temp[len-1];
								}
								else{
									temp3[d] = temp[d-7];
								}
							}
							int val = atoi(temp3.c_str());
							if( val >= up && val <= down)
							{
								elemCount = elemCount + 1;
			//					output << temp<<"--> ";
			//				    output << temp3<<" ";
								elemList[s] = temp3;
								s = s+1;
						
							}
						}	
	
							if ( len >=9 )
						{
							for (d = 0; d <= len-1; d++){	
							
								if ( d == 0){
									temp3[d] = temp[len-8];
						
								}
								else if ( d == 1){
									temp3[d] = temp[len-7];
								}
								else if ( d == 2){
									temp3[d] = temp[len-6];
								}
								else if ( d == 3){
									temp3[d] = temp[len-5];
								}
								else if ( d == 4){
									temp3[d] = temp[len-4];
								}
								else if ( d == 5){
									temp3[d] = temp[len-3];
								}
								else if ( d == 6){
									temp3[d] = temp[len-2];
								}
								else if ( d == 7){
									temp3[d] = temp[len-1];
								}
								else{
									temp3[d] = temp[d-8];
								}
							}
							int val = atoi(temp3.c_str());
							if( val >= up && val <= down)
							{
								elemCount = elemCount + 1;
			//					output << temp<<"--> ";
			//					output << temp3<<" ";
								elemList[s] = temp3;
								s = s+1;
							}
						}	
	
				}
	
	
					
			}
			 
	
	
	
	
	
		}
		
	cout <<"--"<<elemCount;
	output<<elemCount;
	output<<endl;		
	}
	
	cout<<endl;
	cout<<endl;
	input.close();
	output.close();
	getch();

}

