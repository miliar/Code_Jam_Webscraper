
#include <windows.h>
#include <stdio.h>

bool PrepareFiles();
bool GetNumberOfCases(int *_numc);
bool SolveProblem(int _case);
void CleanUp();

FILE *fileIn=NULL;
FILE *fileOut=NULL;

struct NAMES
{
	char name[128];
};

struct ENGINE_NAME
{
	struct NAMES engine[100];
};

struct SEARCH_QUERY
{
	struct NAMES search[1000];
};

ENGINE_NAME en;
SEARCH_QUERY sq;

int main()
{
	int numc=0;
	int i;

	if(!PrepareFiles())
	{
		printf_s("PrepareFiles Error !!!\n");
		CleanUp();
		return 0;
	}
	if(!GetNumberOfCases(&numc))
	{
		printf_s("GetNumberOfCases Error !!!\n");
		CleanUp();
		return 0;
	}
	for(i=1;i<numc+1;i++)
	{
		if(!SolveProblem(i))
			printf_s("%s""%d""%s","Unable to solve problem ",i," !!!\n");
	}
	printf_s("%s","Done !\n");
	CleanUp();
	return 0;
}

bool PrepareFiles()
{
	OPENFILENAMEA ofn;
	char fileName[260];
	char outFileName[260];

	memset(&ofn,0,sizeof(ofn));
	ofn.lStructSize=sizeof(ofn);
	ofn.lpstrFilter="Code Jam Input Files\0*.in\0All Files\0*.*\0";
	ofn.nFilterIndex=1;
	ofn.lpstrFile=fileName;
	ofn.nMaxFile=sizeof(fileName);
	ofn.lpstrTitle="Select Input File";
	ofn.Flags=OFN_PATHMUSTEXIST | OFN_FILEMUSTEXIST;
	ofn.lpstrFile[0]='\0';

	if(GetOpenFileNameA(&ofn)==0) 
		return false;
	if(fopen_s(&fileIn,fileName,"r")!=0)
		return false;
	if(strncpy_s(outFileName,sizeof(outFileName),fileName,ofn.nFileExtension)!=0)
		return false;
	if(strcat_s(outFileName,sizeof(outFileName),"out")!=0)
		return false;
	if(fopen_s(&fileOut,outFileName,"w")!=0)
		return false;
	return true;
}

bool GetNumberOfCases(int *_numc)
{
	if(fseek(fileIn,0L,SEEK_SET)!=0)
		return false;
	if(fscanf_s(fileIn,"%d",_numc)==EOF)
		return false;
	return true;
}

void CleanUp()
{
	if(fileIn)
		fclose(fileIn);
	if(fileOut)
		fclose(fileOut);
}

int GetMatchLine(int _engine,int _searches,int _newSwitchLine)
{
	for(int i=_newSwitchLine;i<_searches;i++)
	{
		if(strcmp(en.engine[_engine].name,sq.search[i].name)==0)
			return i;
	}
	return -1;
}

int GetNewSwitchLine(int _engines,int _searches,int _newSwitchLine)
{
	int switchLine;
	int sl=_newSwitchLine;
	for(int i=0;i<_engines;i++)
	{
		switchLine=GetMatchLine(i,_searches,_newSwitchLine);
		if(switchLine==-1)
			return -1;
		if(sl<switchLine)
			sl=switchLine;
	}
	return sl;
}

bool SolveProblem(int _case)
{
	int engines;
	int searches;
	int switchLine=0;
	int result=0;

	memset(&en,0,sizeof(en));
	memset(&sq,0,sizeof(sq));
	if(fscanf_s(fileIn,"%d",&engines)==EOF)
		return false;
	for(int i=0;i<engines;i++)
	{
		if(fgets(en.engine[i].name,128,fileIn)==NULL)
			return false;
		if(i==0)
		{
		if(fgets(en.engine[i].name,128,fileIn)==NULL)
			return false;
		}
	}
	if(fscanf_s(fileIn,"%d",&searches)==EOF)
		return false;
	for(int i=0;i<searches;i++)
	{
		if(fgets(sq.search[i].name,128,fileIn)==NULL)
			return false;
		if(i==0)
		{
		if(fgets(sq.search[i].name,128,fileIn)==NULL)
			return false;
		}
	}
	while(searches-switchLine>=engines)
	{
		switchLine=GetNewSwitchLine(engines,searches,switchLine);
		if(switchLine==-1)
			break;
		result+=1;
	}
	fprintf_s(fileOut,"%s""%d""%s""%d\n","Case #",_case,": ",result);
	return true;
}
