// GoogleDlg.h : header file
//

#pragma once

struct ScheduleEntry
{
	int depHour;
	int depMin;
	int ariHour;
	int ariMin;
	int station; //0 for atob, 1 for btoa

	ScheduleEntry()
	{
		depHour=0;
		depMin=0;
		ariHour=0;
		ariMin=0;
		station=-1;
	}
};

struct TrainEntry
{
	int depHour;
	int depMin;
	int present; //0 for atob, 1 for btoa

	TrainEntry()
	{
		depHour=0;
		depMin=0;
		present=-1;
	}
};


// CGoogleDlg dialog
class CGoogleDlg : public CDialog
{
// Construction
public:
	CGoogleDlg(CWnd* pParent = NULL);	// standard constructor

// Dialog Data
	enum { IDD = IDD_GOOGLE_DIALOG };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support


// Implementation
protected:
	HICON m_hIcon;

	// Generated message map functions
	virtual BOOL OnInitDialog();
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	DECLARE_MESSAGE_MAP()

private:
	int m_na;
	int m_nb;
	int m_trainCount;

	struct ScheduleEntry m_schedule[500];
	struct ScheduleEntry m_sortedSchedule[500];
	struct TrainEntry m_train[500];

	void StartMain();
	void TellTheMin(struct ScheduleEntry* entry);
	void FindTrain(struct ScheduleEntry* entry, int* a, int* b, int turnA);
};
