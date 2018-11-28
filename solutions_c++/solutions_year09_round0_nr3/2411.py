#include<afxwin.h>
#include<iostream.h>

int FindStart(int start[], int llen, int enable[]){
	for(int i=18; i>=0; i--){
		if(enable[i]==0 && (llen-start[i])>(19-i)){
			return i;
		}
		else{
			enable[i]=-1;
		}
	}
	return -1;
}
void Clear(int enable[]){
	for(int i=0; i<19; i++){
		enable[i]=0;
	}
}

int Cal(char * stdStr, char * line, int si, int li, int slen, int llen){
	int count=0;
	if(si==slen-1){
		while(li < llen){
			if(stdStr[si]==line[li]){
				count++;
			}
			li++;
		}
		return count;
	}
	else{
		while(li < llen){
			if(stdStr[si]==line[li]){
				count += Cal(stdStr, line, si+1, li+1,slen, llen);
			}
			li++;
		}
		return count;
	}

	

}
void main()
{
	// Set Path
	CString sample="sample.txt";
	CString small="C-small-attempt0.in";
	CString large="B-large.in";
	CString output="output.txt";

	// Read File
	CStdioFile f_input;
	f_input.Open(small, CStdioFile::modeReadWrite);
	CStdioFile f_output;
	f_output.Open(output, CStdioFile::modeReadWrite|CStdioFile::modeCreate);
	// Read Line
	CString strValue;
	f_input.ReadString(strValue);
	char* line = strValue.GetBuffer(strValue.GetLength());

	char* stdStr = "welcome to code jam";
	// Get Cases
	int N;
	sscanf(line, "%d", &N);
	
	for(int i=0; i<N; i++){
		// Get Case Data
		f_input.ReadString(strValue);
		line = strValue.GetBuffer(strValue.GetLength());
	


		
		
		// Calculate the count
		int si=0, li=0;
		int count=0;
		int slen=0, llen=0;
		slen=strlen(stdStr);
		llen=strlen(line);
		count= Cal(stdStr, line, si, li,slen, llen);
		/*int startIndex=0;

		// Set Flag
		int enable[19]={0}; //0=true
		int start[19]={0};
		printf("Case #%d: %s\n", i+1, line);
		while(li<llen){
			if(stdStr[si]==line[li]){
				// Match start
				start[si]=li;
				// Match end
				if(si==slen-1){
					count++;
					startIndex=FindStart(start, llen, enable);
					Clear(enable);
					li=start[startIndex]+1;
					si=startIndex;
					continue;
				}
				si++;
			}
			li++;Match
			// No 
			if(li>=llen){
				enable[startIndex]=-1;
				startIndex=FindStart(start, llen, enable);
				Clear(enable);
				li=start[startIndex]+1;
				si=startIndex;
			}
		}

		//if(count >0){}*/

		// Output
		char out[5]="0000";
		for(int j=0; j<4; j++){
			int temp = count%10;
			count/=10;
			out[3-j]+=temp;
		}
		//printf("Case #%d: %s\n", i+1, out);
		
		// Write File
		CString strWriteValue;
		strWriteValue.Format("Case #%d: %s\n", i+1, out);
		f_output.WriteString(strWriteValue);
		
		
	}
	f_input.Close();
	f_output.Close();
	
}