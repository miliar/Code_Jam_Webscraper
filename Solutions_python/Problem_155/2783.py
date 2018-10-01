import java.io.PrintWriter

import scala.io.Source

val out = new PrintWriter("/Users/myair/IdeaProjects/scala/hello/src/main/scala/output.txt")
val lines = Source
  .fromFile("/Users/myair/IdeaProjects/scala/hello/src/main/scala/A-large.in")
  .getLines().toArray[String]

for (i <- 1 to lines.length - 1) {
  val peopleLabelsArray = lines(i).split(" ")(1).toCharArray.map(_.toString.toInt)
  out.write("Case #" + i + ": " + friendsCounter(0, peopleLabelsArray, 0, 0) + "\n")
}

def friendsCounter(position: Int,
                   peopleLabelsArray: Array[Int],
                   sumOfPeople: Int,
                   friends: Int): Int = {
  if (position == peopleLabelsArray.length) friends
  else if (sumOfPeople >= position) friendsCounter(position + 1, peopleLabelsArray, sumOfPeople + peopleLabelsArray(position), friends)
  else friendsCounter(position, peopleLabelsArray, sumOfPeople + 1, friends + 1)
}

out.close()