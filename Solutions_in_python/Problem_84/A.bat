@echo off
if not exist "%~n0.py" echo [!] missing '%~n0.py' 1>&2 && exit 1
:: if not exist "%~n0.zip" echo [*] archive '%~n0.zip' && zip -jo9T "%~n0.zip" "%~n0.py" "%~0" coderun.py codejam.py | sed "s/^ */    /"
call :test large   %*
call :test large-0 %*
call :test large-practice %*
call :test small   %*
call :test small-0 %*
call :test small-1 %*
call :test small-2 %*
call :test small-3 %*
call :test small-practice %*
python -O "%~n0.py" %*
goto :eof

:test
call :test2 "%~n0-%~1" %2 %3 %4 %5
goto :eof
:test2
if not exist "%~1.in" echo [-] %~1
if not exist "%~1.in" goto :eof
if exist "%~1.out"    echo [+] %~1
if exist "%~1.out"    goto :eof
echo [*] %~1   %2 %3 %4 %5
python -O "%~n0.py" -t %2 %3 %4 %5 "%~1.in"
set rc=%errorlevel%
if exist "%~1.out" if exist "%~1.good" echo [*] compare output to '%~1.good' && diff -w "%~1.out" "%~1.good"
exit %rc%
