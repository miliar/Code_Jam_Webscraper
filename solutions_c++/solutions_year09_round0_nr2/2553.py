#include<afxwin.h>
#include<iostream.h>
#define MAX_LENGTH 1024

typedef struct{
	int x;
	int y;
}Point;

Point FindLowestCell(int **data, Point p, int H, int W){
	Point result={0, 0};
	result.x=p.x;
	result.y=p.y;
	int min=data[p.x][p.y];

	// North
	if(p.x>0 && min>data[p.x-1][p.y]){
		min=data[p.x-1][p.y];
		result.x=p.x-1;
		result.y=p.y;
	}
	// West
	if(p.y>0 && min>data[p.x][p.y-1]){
		min=data[p.x][p.y-1];
		result.x=p.x;
		result.y=p.y-1;
	}
	// East
	if(p.y<W-1 && min>data[p.x][p.y+1]){
		min=data[p.x][p.y+1];
		result.x=p.x;
		result.y=p.y+1;
	}
	// South
	if(p.x<H-1 && min>data[p.x+1][p.y]){
		min=data[p.x+1][p.y];
		result.x=p.x+1;
		result.y=p.y;
	}
	return result;
}
char CalBasin(char**altitude, int **data, Point p, int H, int W, char basinIndex){
	Point lowest={0, 0};
	lowest = FindLowestCell(data, p, H, W);
	if(altitude[lowest.x][lowest.y]==0){
		
		if(lowest.x==p.x && lowest.y==p.y){
			altitude[p.x][p.y]=basinIndex;
			return basinIndex;
		}
		else{
			altitude[p.x][p.y]=CalBasin(altitude, data, lowest, H, W, basinIndex);
			return altitude[p.x][p.y];
		}
	}
	else{
		altitude[p.x][p.y]= altitude[lowest.x][lowest.y];
		return altitude[p.x][p.y];
	}
}

void main()
{
	// Set Path
	CString sample="sample.txt";
	CString small="B-small-attempt3.in";
	CString large="B-large.in";
	CString output="output.txt";

	// Read File
	CStdioFile f_input;
	f_input.Open(large, CStdioFile::modeReadWrite);
	CStdioFile f_output;
	f_output.Open(output, CStdioFile::modeReadWrite|CStdioFile::modeCreate);
	// Read Line
	CString strValue;
	f_input.ReadString(strValue);
	char* line = strValue.GetBuffer(strValue.GetLength());

	int **data;
	data=new int *[100];
	char **altitude;
	altitude=new char *[100];
	for(int i=0;i<100;i++)
	{
		altitude[i]=new char[100];
		for(int j=0; j<100; j++){
			altitude[i][j]=0;
		}
		data[i]=new int[100]; 

	}

	// Get Cases
	int T, H, W;
	sscanf(line, "%d", &T);
	for(i=0; i<T; i++){
		if(i==1)
		{
			int a=0;
		}
		// Get Height and Width
		f_input.ReadString(strValue);
		line = strValue.GetBuffer(strValue.GetLength());
		sscanf(line, "%d %d", &H, &W);
		//cout<<"H and W"<<H<<' '<<W<<endl;
		
		for(int j=0;j<H;j++){
			for(int k=0; k<W; k++){
				altitude[j][k]=0;
			}
		}

		// Get Data
		for(j=0; j<H; j++){
			f_input.ReadString(strValue);
			line = strValue.GetBuffer(strValue.GetLength());
			int index=0;
			for(int k=0; k<W; k++){
				sscanf(line+index, "%d", &data[j][k]);
				while(line[index]!=' '){
					index++;
				}
				index++;
				//cout<<data[j][k]<<' ';
			}
			//cout<<endl;
		}


		// Calculate Watersheds
		char basinIndex='a'-1;
		char temp=0;
		for(j=0; j<H; j++){
			for(int k=0; k<W; k++){
				if(altitude[j][k]==0){
					Point curPoint={0, 0};
					curPoint.x=j;
					curPoint.y=k;
					temp = CalBasin(altitude, data, curPoint, H, W, basinIndex+1);
					if(temp == basinIndex+1)
						basinIndex++;
				}
			}
		}
		
	
		// Write File
		CString strWriteValue;
		strWriteValue.Format("Case #%d:\n",i+1);
		f_output.WriteString(strWriteValue);
		for(j=0; j<H; j++){
			strWriteValue="";
			CString temp="";
			for(int k=0; k<W; k++){
				temp.Format("%c", altitude[j][k]);
				strWriteValue+=temp;
				if(k<W-1)
					strWriteValue+=" ";
			}
			strWriteValue+="\n";
			f_output.WriteString(strWriteValue);
		}
		
	}
	f_input.Close();
	f_output.Close();
	
}