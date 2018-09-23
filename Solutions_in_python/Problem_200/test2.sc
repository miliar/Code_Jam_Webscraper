import java.io.{File, PrintWriter}

import scala.io.Source

val fileName = "/Users/inna/scala/Study/Spark_Scala/untitled/B-large.txt"
val pw = new PrintWriter(new File("/Users/inna/scala/Study/Spark_Scala/untitled/out2.txt" ))
var changed = false
def tidyNum(n:String): String ={
  val num = n.map(_.toString.toInt)
  var i = 0
  while (i+1< n.size && num(i)<=num(i+1)){
    i+=1
  }
  if (i>=0 && i!=num.size-1 )
  num.zipWithIndex.map{case (el,ind)=>{
    if (ind < i ) el
    else if (ind==i  ) el -1
    else 9
  }}.mkString
  else n
}

def res (inp: String): Long = {
  if(inp.size==1) inp.toLong
  else {
  var res = tidyNum(inp)
  while (res != tidyNum(res)){
    res = tidyNum(res)
  }
  res.toLong}
}



val lines =  Source.fromFile(fileName).getLines().toList
for (t <- (1 to lines.size-1)) {
  val num = lines(t)
  val r = res(num)
  pw.write(s"Case #${t}: ${r}\n")

}
pw.close